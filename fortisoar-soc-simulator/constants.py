LOGGER_NAME = 'soc_scenario'
CONNECTOR_VERSION = '1.0.9'
INDICATOR_JSON_PAYLOAD = {
    "value": "",
    "typeofindicator": "/api/3/picklists/0162241b-f5bf-4917-a150-00e920be47bd",
    "tlp": "/api/3/picklists/7bff95b7-6438-4b01-b23a-0fe8cb5b33d3",
    "indicatorStatus": "/api/3/picklists/2f5cff61-fbff-4bb3-96be-302b78a9fb47",
    "file": "",
    "conflict": False
}
PHISHING_PHRASE = 'Please note: All users are required to fill the above details and send it to our IT service provider [{EMAIL}] within 3 days from receiving the notification. For more details please visit : [{URL}]'
FIELDS_TO_DELETE = ['uuid','@id','id','respDueDate','ackDate','respDate','dueBy','sourceId','state']
MALICIOUS_FILE_B64 = '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'