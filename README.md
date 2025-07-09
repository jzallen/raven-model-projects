# raven-model-projects

## Development Environment

This project is configured to work seamlessly with Gitpod, providing a cloud-based development environment that's ready to use in seconds.

### Gitpod Setup

#### Quick Start
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/your-username/raven-model-projects)

Click the button above to open this project in Gitpod with a fully configured development environment.

#### Environment Configuration

**Container Base**: Python 3.12 Development Container
- Uses Microsoft's official Python 3.12 dev container image
- Includes Git built from source and pre-installed
- Configured for the `vscode` user

**Pre-installed Tools & Extensions**:
- Python 3.12 with pip (automatically upgraded)
- Black code formatter
- Flake8 linter
- Pytest testing framework
- VS Code extensions:
  - Python language support
  - Black formatter integration
  - Pylance (advanced Python language server)
  - GitLens for enhanced Git integration

**Development Features**:
- Format on save enabled (using Black)
- Python linting enabled with Flake8
- Pytest testing framework ready to use
- Default Python interpreter: `/usr/local/bin/python`

#### Gitpod Automations

The project includes automated setup tasks through `.gitpod/automations.yaml`:

**Dependencies Installation**:
- Automatically upgrades pip to the latest version
- Can be triggered manually when needed
- Ensures consistent package management

#### Getting Started

1. **Using Gitpod**: Click the "Open in Gitpod" button above
2. **Using Dev Containers locally**: Open in VS Code with the Dev Containers extension
3. **Manual setup**: Follow the commands in the postCreateCommand from devcontainer.json

The environment will automatically:
- Set up Python 3.12
- Install and upgrade pip
- Configure code formatting and linting
- Set up testing framework
- Configure VS Code with recommended extensions and settings
