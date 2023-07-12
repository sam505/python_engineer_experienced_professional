from main import *


def test_one_read_json():
    filepath = "data/data_1.json"

    actual_data = {
    "attributes": {
      "appName": "ABCDEFG",
      "eventType": "ABCDEFGHIJ",
      "subEventType": "ABCDEFGHIJKLMNOPQRSTU",
      "sensitive": True
    },
    "message": {
      "battle": {
        "id": "ABCDEFGHIJKLMNOPQR",
        "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNO",
        "settings": {
          "minParticipants": 942,
          "maxParticipants": 641,
          "battleType": "ABCDEFGHIJKLMN",
          "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
          "countdown": 69,
          "duration": 200,
          "archetype": {
            "name": "ABCDEFGHIJKLMNOPQRS",
            "iconId": "ABCDEFGHIJKLMNOPQRST"
          }
        },
        "status": "ABCDEFGHIJKL",
        "creationTime": 240,
        "startTime": 626,
        "endTime": 353,
        "creator": {
          "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
          "nickname": "ABCDEFGHIJKLMNOPQ",
          "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "accountType": "ABCDE",
          "countryCode": "ABCD",
          "orientation": "ABCDEFGHIJKLMNO"
        },
        "participants": [
          {
            "user": {
              "id": "ABCDEFGHIJKLMN",
              "nickname": "ABCDEFGHIJKLMN",
              "title": "ABCDEFGHIJK",
              "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
              "countryCode": "ABCDEFGH",
              "orientation": "ABCDEFGHIJKLMNOPQRSTUVWXY"
            },
            "creator": False,
            "ranking": 498,
            "numberOfTrades": 862,
            "performance": "ABCDEFGHIJKLMNOPQRSTUVW"
          }
        ]
      },
      "joiner": {
        "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB",
        "nickname": "ABCDEFGHIJKLMNO",
        "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
        "accountType": "ABCDEFGHIJKLMNOPQRS",
        "countryCode": "ABCDEFGHIJKLMNOPQR",
        "orientation": "ABCDEFGHIJKLMNOPQR"
      },
      "participantIds": [
        "ABCDEFGHIJKLMNOPQRST",
        "ABCDEFGHIJKLMNOPQRSTUVWXY"
      ]
    }
  }
    
    read_data = read_json(filepath)

    assert actual_data == read_data


def test_two_read_json():
    filepath = "data/data_not_exist.json"
    
    read_data = read_json(filepath)

    assert read_data is None