import requests
import json
from loguru import logger

url = "https://gql.api.mattglei.ch"
payload = '{"query":"{\\n  socials {\\n    github {\\n      username\\n      description\\n      url\\n    }\\n    twitter {\\n      username\\n      description\\n      url\\n    }\\n    dockerHub {\\n      username\\n      description\\n      url\\n    }\\n    linkedin {\\n      username\\n      description\\n      url\\n    }\\n    productHunt {\\n      username\\n      description\\n      url\\n    }\\n    strava {\\n      username\\n      description\\n      url\\n    }\\n    wakatime {\\n      username\\n      description\\n      url\\n    }\\n    reddit {\\n      username\\n      description\\n      url\\n    }\\n  }\\n}","variables":{}}'
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)
if not response.ok:
    logger.critical(f"Failed to make request with response of {response.status_code}")
    exit(1)

data = response.json()["data"]["socials"]

with open("../routes.json", "w") as routes_file:
    json.dump(
        [
            {
                "name": "d",
                "title": "Docker Hub",
                "description": data["dockerHub"]["description"],
                "public": True,
                "url": data["dockerHub"]["url"],
            },
            {
                "name": "g",
                "title": "GitHub",
                "description": data["github"]["description"],
                "public": True,
                "url": data["github"]["url"],
            },
            {
                "name": "l",
                "title": "Linkedin",
                "description": data["linkedin"]["description"],
                "public": True,
                "url": data["linkedin"]["url"],
            },
            {
                "name": "s",
                "title": "Strava",
                "description": data["strava"]["description"],
                "public": True,
                "url": data["strava"]["url"],
            },
            {
                "name": "t",
                "title": "Twitter",
                "description": data["twitter"]["description"],
                "public": True,
                "url": data["twitter"]["url"],
            },
            {
                "name": "w",
                "title": "Wakatime",
                "description": data["wakatime"]["description"],
                "public": True,
                "url": data["wakatime"]["url"],
            },
            {
                "name": "r",
                "title": "Reddit",
                "description": data["reddit"]["description"],
                "public": True,
                "url": data["reddit"]["url"],
            },
            {
                "name": "p",
                "title": "Product Hunt",
                "description": data["productHunt"]["description"],
                "public": True,
                "url": data["productHunt"]["url"],
            },
        ],
        routes_file,
    )

logger.success("Wrote to ../routes.json")
