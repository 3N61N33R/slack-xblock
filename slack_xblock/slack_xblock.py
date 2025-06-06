"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files
import pkg_resources

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String


class SlackXBlock(XBlock):
    """
    An XBlock that displays a button/link to a Slack channel.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    # Fields for configuration in Studio
    display_name = String(
        default="Slack Channel Link",
        scope=Scope.settings,
        help="The name shown in Studio for this XBlock.",
    )
    slack_channel_url = String(
        default="https://slack.com/",  # Default placeholder
        scope=Scope.settings,
        help="The full URL to the Slack channel (e.g., https://yourworkspace.slack.com/archives/C1234567890)",
    )
    button_text = String(
        default="Join Our Slack Channel",
        scope=Scope.settings,
        help="Text to display on the button.",
    )
    description_text = String(
        default="For real-time discussions and quick questions, join our dedicated Slack channel:",
        scope=Scope.settings,
        help="Introductory text displayed above the button.",
    )

    def resource_string(self, path):
        """Handy helper for loading resources from our package."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def render_template(self, template_path, context={}):
        """Renders a Jinja2 template."""
        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader(self.runtime.handler_path))
        template = env.get_template(template_path)
        return template.render(context)

    def student_view(self, context=None):  # pylint: disable=W0613
        """
        The primary view of the XBlock, shown to students when viewing courses.
        """
        html = self.resource_string("static/html/slack_xblock.html")
        frag = Fragment(
            html.format(
                slack_channel_url=self.slack_channel_url,
                button_text=self.button_text,
                description_text=self.description_text,
            )
        )
        frag.add_css(self.resource_string("static/css/slack_xblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/slack_xblock.js"))
        frag.initialize_js("SlackXBlock")  # Initialize the JavaScript for this XBlock
        return frag

    def studio_view(self, context=None):
        """
        The view of the XBlock in Open edX Studio for authors to configure.
        """
        html = self.resource_string("static/html/slack_xblock_edit.html")
        frag = Fragment(
            html.format(
                slack_channel_url=self.slack_channel_url,
                button_text=self.button_text,
                description_text=self.description_text,
                display_name=self.display_name,
            )
        )
        frag.add_css(self.resource_string("static/css/slack_xblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/slack_xblock_edit.js"))
        frag.initialize_js("SlackLinkXBlockStudio")
        return frag

    @XBlock.json_handler
    def submit_edits(self, data, suffix=""):
        """
        Handles saving changes from the Studio edit view.
        """
        self.slack_channel_url = data.get("slack_channel_url")
        self.button_text = data.get("button_text")
        self.description_text = data.get("description_text")
        self.display_name = data.get("display_name")
        return {"result": "success"}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            (
                "SlackXBlock",
                """<slack_xblock/>
             """,
            ),
            (
                "Multiple SlackXBlock",
                """<vertical_demo>
                <slack_xblock/>
                <slack_xblock/>
                <slack_xblock/>
                </vertical_demo>
             """,
            ),
        ]
