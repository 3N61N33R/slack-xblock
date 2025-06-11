# Slack XBlock for Open edX

An XBlock that integrates Slack channels directly into Open edX courses, enabling seamless communication between course content and discussions.

## Features

- 🚀 Easy integration with existing Slack workspaces
- 🎯 Auto-generated channel names based on course context
- 🎨 Responsive, modern UI design
- ⚙️ Studio-configurable settings
- 📊 Optional analytics and tracking
- 🔧 Flexible channel management

## Installation

### Development

```bash
git clone git@github.com:3N61N33R/slack-xblock.git
cd slack-xblock
pip install -e .
```

### Production

```bash
pip install slack-xblock
```

## Configuration

1. Add to Open edX settings:

```python
INSTALLED_APPS += ['slack_xblock']
FEATURES['ENABLE_SLACK_XBLOCK'] = True
```

2. Configure in Studio:

- Add Slack component to course units
- Set workspace URL and channel settings
- Customize display options

## Usage

For detailed usage instructions, see the [Installation Guide](docs/installation.md).

## License

---
