from pytrends.request import TrendReq


def get_trending_keywords():

    pytrends = TrendReq(hl="en-US", tz=330)

    keywords = [
        "athlete training",
        "sports recovery",
        "sports technology",
        "injury prevention",
        "sports performance"
    ]

    pytrends.build_payload(keywords, timeframe="now 7-d")

    related = pytrends.related_queries()

    results = []

    for key in related:
        if related[key]["top"] is not None:

            df = related[key]["top"]

            for query in df["query"].head(5):
                results.append(query)

    results = list(set(results))

    return results[:15]