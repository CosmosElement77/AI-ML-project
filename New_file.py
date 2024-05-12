from Imports import *

credits_df=pd.read_csv('credits.csv')
movies_df=pd.read_csv('movies.csv')

pd.set_option("display.max_columns",None)
# pd.set_option("display.max_colwidth" , None)
pd.set_option("display.max_rows",None)

movies_df = movies_df.merge(credits_df , on='title')
movies_df = movies_df[['movie_id' ,'genres' ,'title' ,'overview', 'tagline' , 'cast' ,'keywords' , 'release_date']]
# movies_df.head()
movies_df.dropna(inplace=True)
# movies_df.info()# print(movies_df.genres.get("name"))  #movies_df.genres.name.value   #why not working ?

#Using the user defined convert and convert_cast function in the Imports file
movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)
movies_df['cast'] = movies_df['cast'].apply(convert_cast)

# Using the join_b user defined function to remove the [] brackets
movies_df['genres'] = movies_df['genres'].apply(join_b)
movies_df['cast'] = movies_df['cast'].apply(join_b)
movies_df['keywords'] = movies_df['keywords'].apply(join_b)


movies_df['tags']=movies_df['genres'] +" ; " + movies_df['keywords'] +" ; " + movies_df['overview'] +" ; " + movies_df['tagline'] +" ; " + movies_df['cast']

#making a new dataFrame for poratbility and assigining the cosine similarity (used to compare two variables)
#Convert a collection of text documents to a matrix of token counts.
new_df=movies_df[['movie_id','genres','title','tags','release_date']]
cv=CountVectorizer(max_features=5000,stop_words='english')
cv.fit_transform(new_df['tags']).toarray()
vector_similarity=cv.fit_transform(new_df['tags']).toarray()
vector_similarity[0]

#remove suffixes from english words and obtain the stem(a part of a word common to all its variants)
ps=PorterStemmer()
def stem(input):
    input_list=[]
    for i in input.split():
        input_list.append(ps.stem(i))
    return " ".join(input_list)

new_df['tags']=new_df['tags'].apply(stem)
# cosine_similarity(vector_similarity)
Similar_Choices=cosine_similarity(vector_similarity)

def recommend(movie_name ):
    movie_index=new_df[new_df['title']==movie_name].index[0] 
    distances= Similar_Choices[movie_index]
    movies_list =sorted(list(enumerate (distances)), reverse=True, key=lambda x:x[1]) [1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

recommend("Avatar")


#A value is trying to be set on a copy of a slice from a DataFrame.
#Try using .loc[row_indexer,col_indexer] = value instead