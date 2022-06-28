from data_preview_and_recommendation_system import sim_jaccard,topMatches,getRecommendations,movies
def main():
    print(f"{movies}\n")
    print(f"Star Wars (1977) filmine en çok benzeyen 5 film:\n{topMatches(movies,'Star Wars (1977)', 5, sim_jaccard)}")
    print(f"\nLion King, The (1994) filmine en çok benzeyen 5 film:\n{topMatches(movies,'Lion King, The (1994)', 5, sim_jaccard)}")
    print(f"\nGodfather, The (1972) filmine en çok benzeyen 5 film:{topMatches(movies,'Godfather, The (1972)', 5, sim_jaccard)}")
    print(f"\nCrossing Guard, The (1995) filmi için önerilecek türler: \n{getRecommendations(movies, 'Crossing Guard, The (1995)')}")
main()