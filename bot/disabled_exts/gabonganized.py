"""
    Gabonganized

    Allows users to right click face pictures and
    gabonganize them, and also has random gabonganizing effects

    Made with love and care by Vaughn Woerpel
"""

# built-in
import logging

# external
import discord
from discord import app_commands
from discord.ext import commands
from wand.image import Image

# project modules
from bot.utils import file_helper, magick_helper

log = logging.getLogger("gabonganized")


class Gabonga(commands.Cog):
    """Gabonga class to handle all gabonga requests"""

    def __init__(self, bot: commands.Bot) -> None:
        """Intializes the 'bonga class and assigns the command tree for the 'bonga menu"""
        self.bot = bot

        self.gabonga_menu = app_commands.ContextMenu(
            name="gabonga", callback=self.gabonga_menu
        )
        self.bot.tree.add_command(self.gabonga_menu)

    async def gabonga_menu(
        self, interaction: discord.Interaction, message: discord.Message
    ) -> None:
        """Controls the bonga menu"""

        await interaction.response.defer()
        response = await gabonga_helper(message)

        match response:
            case "Message had no file":
                await interaction.followup.send("That message didn't have a file!!")
                return
            case "Invalid filetype":
                await interaction.followup.send(
                    "Silly fool! 'bonga only works on portable network graphics and and joint photographic experts group :nerd:"
                )
                return
            case "No faces in image":
                log.info(f"No faces in bonga request")
                await interaction.followup.send(
                    "Egads!!! There are no faces in that 'bonga request! Why don't you try another :smirk_cat:"
                )
                return
            case "Gabonga failure":
                log.error(f"Failure while trying to gabonganize image/gif")
                await interaction.followup.send("Gabonga has mysteriously failed")
                return

        log.info(f"Image was succesfully gabonganized: {response})")
        await interaction.followup.send(
            content="I have two words...", file=discord.File(response)
        )
        file_helper.remove(response)


async def gabonga_helper(message: discord.Message) -> str:
    """Helper method to help with gabonga requests"""

    # Grabs and checks file
    fname = file_helper.grab(message)
    if fname is None:
        return "Message had no file"

    # Checks filetype
    if not fname.endswith((".png", ".jpg", ".jpeg")):
        file_helper.remove(fname)
        return "Invalid filetype"

    # Uses face rec to grab the face and get the location
    face_locations = await magick_helper.get_faces(fname)
    if len(face_locations) == 0:
        file_helper.remove(fname)
        return "No faces in image"

    gabonganized = await gabonga(fname, face_locations)

    if gabonganized is not None:
        return gabonganized
    else:
        file_helper.remove(fname)
        return "Gabonga failure"


async def gabonga(fname: str, face_locations: list) -> str:
    """Handles the actual editing work of gabonga"""

    with Image(filename=fname) as face:
        with Image(filename="bot/resources/gabonga.png") as gabonga:
            # Tries to do multiple faces... might not work
            for face_location in face_locations:
                # Print the location of each face in this image
                x, y, w, h = face_location

                # Resize the 'bonga PNG
                gabonga.resize(w, h)

                # Composites gabonga on top
                face.composite(gabonga, left=x, top=y)
            face.save(filename=fname)
    return fname


async def setup(bot: commands.Bot) -> None:
    """Sets up the cog"""

    await bot.add_cog(Gabonga(bot))
    log.info("Loaded")
