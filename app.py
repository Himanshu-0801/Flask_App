from flask import Flask

app = Flask(__name__)


# create the idea repositiory 

ideas = {
    1:{
        "id" :1,
        "idea_name":"Synergy",
        "idea_description":"details about the synergy team",
        "idea_author":"Himanshu"
   }, 
    2:{
        "id" :2,
        "idea_name":"saving soil",
        "idea_description":"details about the saving the soil",
        "idea_author":"sonu"
    }
}

# create an restful api fetching all the ideas 
@app.get("/ideaapp/api/v1/ideas")

def get_all_ideas():
    #logic to fetch all the ideas
 return ideas




if __name__ =='__main__':
    app.run(port= 8080)