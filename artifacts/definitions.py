# -*- coding: utf-8 -*-
"""Constants and definitions."""

# The type indictor constants.
TYPE_INDICATOR_ARTIFACT = 'ARTIFACT'
TYPE_INDICATOR_COMMAND = 'COMMAND'
TYPE_INDICATOR_DIRECTORY = 'DIRECTORY'
TYPE_INDICATOR_ENVIRONMENT = 'ENVIRONMENT'
TYPE_INDICATOR_FILE = 'FILE'
TYPE_INDICATOR_PATH = 'PATH'
TYPE_INDICATOR_WINDOWS_REGISTRY_KEY = 'REGISTRY_KEY'
TYPE_INDICATOR_WINDOWS_REGISTRY_VALUE = 'REGISTRY_VALUE'
TYPE_INDICATOR_WMI_QUERY = 'WMI'

LABELS = {
    'Antivirus': 'Antivirus related artifacts, e.g. quarantine files.',
    'Authentication': 'Authentication artifacts.',
    'Browser': 'Web Browser artifacts.',
    'Cloud': 'Cloud applications artifacts.',
    'Cloud Storage': 'Cloud storage artifacts.',
    'Configuration Files': 'Configuration files artifacts.',
    'Execution': 'Contain execution events.',
    'ExternalAccount': 'Information about any users\' account, e.g. username, account ID, etc.',
    'External Media': 'Contain external media data or events e.g. USB drives.',
    'KnowledgeBase': 'Artifacts used in knowledge base generation.',
    'IM': 'Instant Messaging / Chat applications artifacts.',
    'iOS' : 'Artifacts related to iOS devices connected to the system.',
    'Logs': 'Contain log files.',
    'Mail': 'Mail client applications artifacts.',
    'Memory': 'Artifacts retrieved from memory.',
    'Network': 'Describe networking state.',
    'Processes': 'Describe running processes.',
    'Software': 'Installed software.',
    'System': 'Core system artifacts.',
    'Users': 'Information about users.',
    'Rekall': 'Artifacts using the Rekall memory forensics framework.',
    }

SUPPORTED_OS = frozenset(['Darwin', 'Linux', 'Windows'])

TOP_LEVEL_KEYS = frozenset(['conditions', 'doc', 'labels', 'name', 'provides',
                            'sources', 'supported_os', 'urls'])
