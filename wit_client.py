from wit import Wit

token = "VJ56M3RHCYN26M6EPKA3S4XTE5EHMDSU"

class wit_client(object):
    def __init__(self, token):
        self._token = token
        self._client = Wit(self._token)
        self.dishes_name = ["soup_name", "pizza_name", "salad_name", "burger_name"]

    def _get_max_proba(self, list):
        p = -1
        ans = ""
        for dic in list:
            if dic["confidence"] > p:
                p = dic["confidence"]
                ans = dic["value"]
        return ans

    def get_dishes_list(self, text):
        resp = self._client.message(text)
        respi = None
        if resp.get("entities") != None:
            respi = dict()
            respi["intent"] = self._get_max_proba(resp["entities"]["intent"])
            mb_dishes = []
            for dish_name in self.dishes_name:
                if resp["entities"].get(dish_name) != None:
                    mb_dishes += resp["entities"].get(dish_name)
            respi["dish"] = self._get_max_proba(mb_dishes)
        return respi


wit = wit_client(token)

wit.get_dishes_list("салат греческий")