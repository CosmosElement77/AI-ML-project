from Imports import *

credits_df=pd.read_csv('credits.csv')
movies_df=pd.read_csv('movies.csv')

pd.set_option("display.max_columns",None)
pd.set_option("display.max_colwidth" , None)
pd.set_option("display.max_rows",None)

movies_df = movies_df.merge(credits_df , on='title')
movies_df = movies_df[['movie_id' ,'genres' ,'title' ,'overview', 'tagline' , 'cast' ,'keywords' , 'release_date','vote_average','crew']]
# movies_df.head()
movies_df.dropna(inplace=True)
# movies_df.info()

#Using the user defined convert and convert_cast function in the Imports file
movies_df['genres'] = movies_df['genres'].apply(convert)
# movies_df['title']=movies_df['title'].apply(makelower)
movies_df['keywords'] = movies_df['keywords'].apply(convert)
movies_df['cast'] = movies_df['cast'].apply(convert_cast)
movies_df['crew'] = movies_df['crew'].apply(find_director)

#Removing space between words
movies_df['genres'] = movies_df['genres'].apply(lambda x:[i.replace(" ","") for i in x])

# Using the join_b user defined function to remove the [] brackets
movies_df['genres'] = movies_df['genres'].apply(join_b)
movies_df['cast'] = movies_df['cast'].apply(join_b)
movies_df['keywords'] = movies_df['keywords'].apply(join_b)
movies_df['crew'] = movies_df['crew'].apply(join_b)

movies_df['tags']= movies_df['overview']+ movies_df['genres']  + movies_df['keywords'] + movies_df['cast'] +movies_df['crew']+movies_df['tagline']

#making a new dataFrame for poratbility and assigining the cosine similarity (used to compare two variables)
#Convert a collection of text documents to a matrix of token counts.
new_df=movies_df[['title','genres','keywords','tags','release_date' ,'vote_average','tagline']]
cv=CountVectorizer(max_features=5000,stop_words='english')
cv.fit_transform(new_df['tags']).toarray()
vector_similarity=cv.fit_transform(new_df['tags']).toarray()
vector_similarity[0]

#remove suffixes from english words and obtain the stem(a part of a word common to all its variants)
ps=PorterStemmer()
def stem(input):
    input_list=[]
    for i in input.split():
        input_list.append(ps.stem(i))#append similar words into a list 
    return " ".join(input_list)#Join the similar words of the list to make a new string 

new_df['tags']=new_df['tags'].apply(stem)
# cosine_similarity(vector_similarity)
Similar_Choices=cosine_similarity(vector_similarity)

def recommend(movie_name ):
    try:
        movie_index=new_df[new_df['title']==movie_name].index[0] 
        movie_index=new_df[new_df['title']==movie_name].index[0] 
        distances= Similar_Choices[movie_index]
        movies_list =sorted(list(enumerate (distances)), reverse=True, key=lambda x:x[1]) [1:6]

        print("\n")
        print(f"The Top 5 Recommended Movies for {movie_name} fans are: \n")
        for i in movies_list:
            print(new_df.iloc[i[0]].title + " ("+new_df.iloc[i[0]].tagline +")"+ "\n" + new_df.iloc[i[0]].release_date +"\n"+new_df.iloc[i[0]].genres +"\n"+str(new_df.iloc[i[0]].vote_average)+"⭐") 
            print("\t")
            print("-------------------------------------------------------------------------------------------")
    except:
        print("\n")
        print("----------------")
        print("|"+"Movie Not Found"+"|")
        print("----------------")
        print("\n")

movie=input("Print the movie name you want recommendations for or type STOP--> ")
while(True):
    if movie!="STOP":
        recommend(movie)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        movie=input("Print the movie name you want recommendations for or type STOP--> ")
    else:
        break
# recommend(movie)


