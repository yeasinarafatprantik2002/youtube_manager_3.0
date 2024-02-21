from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://userid:password@cluster0.8ww9yjr.mongodb.net/", tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
video_collection = db["videos"]
print("Connected to the database\n")


def list_videos():

    videos = video_collection.find()
    print("\nList of videos:")
    print("-" * 70)
    print("         ID                        Title            Time")
    print("-" * 70 + "\n")
    for video in videos:
        print(f"ID: {video["_id"]} - {video['title']} - {video['time']}")
    print("\n" + "-" * 70 )


def add_video(title, time):
    video_collection.insert_one({"title": title, "time": time})


def update_video(video_id, title, time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"title": title, "time": time}})


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    print("Welcome to YouTube Manager")
    while True:
        print("\n//-YouTube Manager-\\\\")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_videos()
            case "2":
                title = input("Enter the title: ")
                time = input("Enter the time: ")
                add_video(title, time)
                print("\nVideo added successfully")
            case "3":
                list_videos()
                video_id = input("Enter the video id: ")
                title = input("Enter the updated title: ")
                time = input("Enter the updated time: ")
                update_video(video_id, title, time)
                print("\nVideo updated successfully")
            case "4":
                list_videos()
                video_id = input("Enter the video id: ")
                delete_video(video_id)
                print("\nVideo deleted successfully")
            case "5":
                print("\nThank you for using YouTube Manager\n")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
