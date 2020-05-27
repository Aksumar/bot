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
        ansi = None
        for dic in list:
            if dic["confidence"] > p:
                p = dic["confidence"]
                ansi = dic.copy()
                ansi.pop("confidence")
        for dic in list:
            if dic["confidence"] == p:
                a = dic.copy()
                a.pop("confidence")
                ans.append(a)
        if not len(ans):
            ans.append(ansi)
        return ans

    def get_dishes_list(self, text):
        resp = self._client.message(text)
        respi = None
        if resp.get("entities").get("intent") is None:
            return {"intent" : None, "dishes" : None, "constructor" : True}
        if not resp.get("entities") is None:
            respi = dict()
            respi["intent"] = self._get_max_proba(resp["entities"]["intent"])
            mb_dishes = {"pizza" : [], "salad" : [], "burger" : []}
            for dish_name in self.dishes_name:
                if not resp["entities"].get(dish_name) is None:
                    for dic in resp["entities"].get(dish_name):
                        dic['value'] = self.trans[dish_name] + " " + dic["value"]
                        dic['type'] = dish_name[:-5]
                    mb_dishes[dish_name[:-5]] += resp["entities"].get(dish_name)
            if not resp["entities"].get("addons") is None:
                respi["addons"] = []
                for dic in resp["entities"].get("addons"):
                    respi["addons"].append(dic['value'])
                for dish in mb_dishes["salad"] + mb_dishes["burger"]:
                    dish["addons"] = respi['addons']
            if not resp["entities"].get("pizza_addons") is None:
                respi["pizza_addons"] = []
                for dic in resp["entities"].get("pizza_addons"):
                    respi["pizza_addons"].append(dic['value'])
                for pizza in mb_dishes["pizza"]:
                    pizza["addons"] = respi['pizza_addons']

        respi["dishes"] = []
        for name in ["pizza", "salad", "burger"]:
            if not self._get_max_proba(mb_dishes[name])[0] is None:
                respi["dishes"] += self._get_max_proba(mb_dishes[name])
        return {"intent" : respi["intent"], "dishes" : respi["dishes"], "constructor" : not len(respi["dishes"])}


if __name__ == "__main__":
    wit = wit_client(token)

    print(wit.get_dishes_list("салат греческий без лука"))