from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from murder_mystery import db

game_app = Blueprint("game", __name__)

## Just some dummy data for now
question_data = {
    "question": "Sample question: Capital of France?",
    "choices": ["Paris", "Tokyo", "Japan"],
}


@game_app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    answers_collection = db["answers"]

    user_id = str(current_user.get_id())

    # Check if the user has already submitted an answer
    answer = answers_collection.find_one({"user_id": user_id})
    if answer:
        return render_template(
            "quiz.html",
            **question_data,
            error="Response not accepted, as you have already submitted once.",
            marked_resp=answer["answer"],
            is_correct_answer=answer["answer"] == "Paris"
        )

    if request.method == "POST":
        user_answer = request.form.get("choice")
        is_correct = user_answer == "Paris"

        # Store the user's answer in the database
        answers_collection.insert_one(
            {"user_id": user_id, "answer": user_answer, "is_correct": is_correct}
        )

        return render_template(
            "quiz.html",
            **question_data,
            user_answer=user_answer,
            is_correct_answer=is_correct,
            marked_resp=user_answer
        )

    return render_template("quiz.html", **question_data, marked_resp=None)
