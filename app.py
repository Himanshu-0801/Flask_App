from flask import Flask, request
# the request is required to request the inserted body from the post
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


'''
// "Create a restful endpoint for creating a new idea"


'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    
    
    # logic to create new idea 
    try:
    # check the request of the new idea 
        request_body = request.get_json( )

     # check if ideas which is passed is already present or not 
        if request_body["id"] and request_body["id"] in ideas:
         return "the idea is already existing in the ideas ",400

    #insert the passed idea in the idea dictionary
        ideas[request_body["id"]] = request_body

    # return the response that idea is submitted 
        return "idea is entered successfully",201 
    except KeyError:
        return "id is missing",400
    except:
        return "Some internal server error",500    

     



if __name__ =='__main__':
    app.run(port= 8080)