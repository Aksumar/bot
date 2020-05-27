from wit import Wit

token = "VJ56M3RHCYN26M6EPKA3S4XTE5EHMDSU"

class wit_client(object):
    def __init__(self, token):
        self._token = token
        self._client = Wit(self._token)
        self.dishes_name = ["soup_name", "pizza_name", "salad_name", "burger_name"]
        self.trans = {"soup_name" : "суп", "pizza_name" : "пицца", "salad_name" : "салат", "berger_name" : "бургер"}

    def _get_max_proba(self, list):
        p = -1
        ans = []
        ansi = ""
        for dic in list:
            if dic["confidence"] > p:
                p = dic["confidence"]
                ansi = dic["value"]
        for dic in list:
            if dic["confidence"] == p:
                ans.append(dic["value"])
        if not len(ans):
            ans.append(ansi)
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
                    for dic in resp["entities"].get(dish_name):
                        dic['value'] = self.trans[dish_name] + " " + dic["value"]
                    mb_dishes += resp["entities"].get(dish_name)
            respi["dish"] = self._get_max_proba(mb_dishes)
            if resp["entities"].get("addons") != None:
                respi["dish"][0] += " " + self._get_max_proba(resp["entities"]["addons"])[0]
                respi["addons"] = []
                for dic in resp["entities"].get("addons"):
                    respi["addons"].append(dic['value'])
        return respi


if __name__ == "__main__":
    wit = wit_client(token)

    print(wit.get_dishes_list("салат греческий без лука"))