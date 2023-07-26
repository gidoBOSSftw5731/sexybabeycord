import os

import discord
from discord import app_commands
from discord.ext import commands
from wand.image import Image
from bot.utils import file
import logging


class Distort(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.distort_menu = app_commands.ContextMenu(
            name="distort", callback=self.distort_ctx
        )
        self.bot.tree.add_command(self.distort_menu)

    async def distort_ctx(
        self, interaction: discord.Interaction, message: discord.Message
    ):
        await interaction.response.defer(ephemeral=True)
        try:
            fname = await file.grab(message)  # Grabs the image
        except Exception:
            await interaction.followup.send(
                "An unexpected error occured while trying to fetch the image."
            )
            return
        if fname is None:
            await interaction.followup.send(
                "The message you tried to distort is either not an image, or is of an invalid type."
            )
            return

        try:
            distort(fname)
        except Exception:
            await interaction.followup.send(
                "An unexpected error occured while trying to distort the image."
            )
            return

        await interaction.followup.send("Done!")
        await interaction.channel.send(
            file=discord.File(fname)
        )
        os.remove(fname)

def distort(fname: str):
    with Image(filename=fname) as temp_img:
        if fname.endswith("gif"):
            with Image() as dst_image:
                with Image(filename=fname) as src_image:
                    src_image.coalesce()
                    for i, frame in enumerate(src_image.sequence):
                        frameimage = Image(image=frame)
                        x, y = frame.width, frame.height
                        if x > 1 and y > 1:
                            frameimage.liquid_rescale(round(x * 0.60), round(y * 0.60))
                            frameimage.resize(x, y)
                            dst_image.sequence.append(frameimage)
                dst_image.optimize_layers()
                dst_image.optimize_transparency()
                dst_image.save(filename=fname)
        else:
            x, y = temp_img.width, temp_img.height
            temp_img.liquid_rescale(round(x * 0.60), round(y * 0.60))
            temp_img.resize(x, y)
            temp_img.save(filename=fname)


async def setup(bot: commands.Bot):
    """Sets up the cog

    Parameters
    -----------
    bot: commands.Bot
    The main cog runners commands.Bot object
    """

    if not os.path.exists("bot/resources/images"):
        os.makedirs("bot/resources/images")

    # Adds the cog and reports that it's loaded
    await bot.add_cog(Distort(bot))
    logging.info("Distort loaded")