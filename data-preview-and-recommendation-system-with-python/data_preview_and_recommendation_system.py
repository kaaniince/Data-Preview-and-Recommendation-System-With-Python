genres = ["Unknown", "Action", "Adventure", "Animation", "Children's",
"Comedy", "Crime", "Documentary", "Drama",
"Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
"Romance", "Sci-Fi", "Thriller", "War", "Western"]
movies={}
from numpy import dot
from numpy.linalg import norm
def create_dict():
    for line in open("u.item.txt"):
        line = line.rstrip('\n')
        new_line = line.split(")|", 1)[0]+")"
        new_line = new_line.split("|", 1)[1]
        movie = new_line.rstrip()
        line = line.rstrip('\n')
        genres_no=line[-37::2]
        genres_no=list(genres_no)
        for i in range(19):
            if genres_no[i]=="1":
                movies.setdefault(movie,{genres[i]:1})
                genre = genres[i]
                movies[movie][genre] = 1
create_dict()

def sim_jaccard(prefs, movie1, movie2):
    m1_intersect_m2 = {}
    for item in prefs[movie1]:
        if item in prefs[movie2]:
            m1_intersect_m2[item] = 1
    m1_union_m2 = dict(prefs[movie1])
    for item in prefs[movie2]:
        if item not in m1_union_m2:
            m1_union_m2[item] = 1
    m1_intersect_m2, m1_union_m2 = len(m1_intersect_m2), len(m1_union_m2)
    return float(m1_intersect_m2) / float(m1_union_m2)

def topMatches(prefs, movie, n=5, similarity=sim_jaccard):
    scores = [(similarity(prefs, movie, other), other)
              for other in prefs if other != movie]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def sim_cosine(prefs, movie1, movie2):
    movie1_moviescores = []
    movie2_moviescores = []
    for item in prefs[movie1]:
        if item in prefs[movie2]:
            movie1_moviescores.append(prefs[movie1][item])
            movie2_moviescores.append(prefs[movie2][item])
    if len(movie1_moviescores) == 0:
        return 0
    cosine = dot(movie1_moviescores, movie2_moviescores) / \
             (norm(movie1_moviescores) * norm(movie2_moviescores))
    return cosine


def getRecommendations(prefs, movie, similarity = sim_cosine):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == movie: continue
        sim = similarity(prefs, movie, other)
        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[movie]:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim
    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
