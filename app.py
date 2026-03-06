from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 데이터 저장소 (서버를 끄면 사라지지만, 지금은 리스트로 연습해 봐요!)
journals = []

@app.route("/")
def index():
    # 저장된 모든 글을 index.html에 전달합니다.
    return render_template("index.html", journals=journals)

@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        # 사용자가 입력한 제목과 내용을 가져옵니다.
        title = request.form.get("title")
        content = request.form.get("content")
        
        if title and content:
            journals.append({"title": title, "content": content})
            
        # 글 작성이 완료되면 메인 페이지로 돌아갑니다.
        return redirect(url_for("index"))
    
    # GET 방식일 때는 글쓰기 페이지를 보여줍니다.
    return render_template("write.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)