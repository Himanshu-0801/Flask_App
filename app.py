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
    idea_author = request.args.get('idea_author')

    if idea_author:
        idea_res ={}
        for key, value in ideas.items():
           if value["idea_author"]== idea_author:  
            idea_res[key]=value
        return idea_res    
    #logic to fetch all the ideas and support query params

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

# end point to fetch idea based on the idea id
# 

@app.get("/ideaapp/api/v1/ideas/<int:idea_id>")  #idea_id is the path param 
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else :
            return "idea_id passed is not present",404    

    except:
        return"some internal error ocurred",500   


'''
Endpoint for updating an idea 

'''
@app.put("/ideaapp/api/v1/ideas/<int:idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id )]= request.get_json()

            return ideas[int(idea_id)],200
        else :
            return "idea_id passed is not present",404    

    except:
        return"some internal error ocurred",500   
 



if __name__ =='__main__':
    app.run(port= 8080)