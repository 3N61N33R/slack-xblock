"""
Configuration settings for Slack XBlock
"""

from decouple import config

try:
    from django.conf import settings as django_settings
except Exception:  # pragma: no cover - Django not available in packaging contexts
    django_settings = None


def _from_django_or_env(name, **config_kwargs):
    """
    Read a setting from Django's settings module first, falling back to env vars.
    """
    if django_settings is not None and hasattr(django_settings, name):
        return getattr(django_settings, name)
    return config(name, **config_kwargs)

# Advanced Configuration Options
SLACK_XBLOCK_ADVANCED_CONFIG = {
    # Slack API integration (future enhancement)
    "SLACK_BOT_TOKEN": _from_django_or_env("SLACK_BOT_TOKEN"),
    "SLACK_SIGNING_SECRET": _from_django_or_env("SLACK_SIGNING_SECRET"),
    # Auto-channel creation settings
    "AUTO_CREATE_CHANNELS": _from_django_or_env(
        "AUTO_CREATE_CHANNELS", default=True, cast=bool
    ),
    "CHANNEL_PREFIX": "course-",
    "CHANNEL_SUFFIX": "-discussion",
    # Default workspace settings
    "DEFAULT_WORKSPACE_URL": _from_django_or_env("DEFAULT_WORKSPACE_URL", default=""),
    "WORKSPACE_INVITE_URL": _from_django_or_env("WORKSPACE_INVITE_URL", default=""),
    # Integration features
    "ENABLE_MEMBER_COUNT": True,
    "ENABLE_ACTIVITY_PREVIEW": True,
    "ENABLE_DIRECT_MESSAGES": False,
    # Analytics and tracking
    "TRACK_CHANNEL_JOINS": True,
    "TRACK_MESSAGE_ACTIVITY": False,
}

# Course-level settings (these go in course advanced settings in Studio)
COURSE_SLACK_SETTINGS_TEMPLATE = {
    "slack_workspace_url": _from_django_or_env("DEFAULT_WORKSPACE_URL", default=""),
    "auto_create_channels": True,
    "channel_naming_pattern": "week-{week_number}",
    "enable_per_unit_channels": False,
    "moderator_roles": ["instructor", "staff"],
}

# Default XBlock settings
DEFAULT_XBLOCK_SETTINGS = {
    "display_name": "Course Discussion on Slack",
    "slack_workspace_url": "",
    "channel_name": "",
    "channel_description": "Course discussion channel",
    "auto_generate_channel": True,
    "show_member_count": True,
}
    