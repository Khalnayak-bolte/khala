from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Application</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family: 'Segoe UI', sans-serif;
}

body{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
    min-height:100vh;
}

header{
    padding:25px 8%;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    font-size:28px;
    font-weight:700;
    color:#38bdf8;
}

nav a{
    color:white;
    text-decoration:none;
    margin-left:30px;
    transition:.3s;
}

nav a:hover{
    color:#38bdf8;
}

.hero{
    min-height:85vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:20px;
}

.hero-content{
    max-width:800px;
}

.hero h1{
    font-size:4rem;
    margin-bottom:20px;
    line-height:1.2;
}

.hero span{
    color:#38bdf8;
}

.hero p{
    font-size:1.2rem;
    color:#cbd5e1;
    margin-bottom:35px;
}

.btn{
    display:inline-block;
    padding:14px 32px;
    background:#38bdf8;
    color:#0f172a;
    text-decoration:none;
    border-radius:50px;
    font-weight:600;
    transition:.3s;
}

.btn:hover{
    transform:translateY(-3px);
    background:#7dd3fc;
}

.features{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:25px;
    padding:0 8% 80px;
}

.card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter:blur(10px);
    padding:30px;
    border-radius:20px;
}

.card h3{
    margin-bottom:12px;
    color:#38bdf8;
}

footer{
    text-align:center;
    padding:30px;
    color:#94a3b8;
}

@media(max-width:768px){
    .hero h1{
        font-size:2.5rem;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">AWS Cloud App</div>

    <nav>
        <a href="#">Home</a>
        <a href="#">Services</a>
        <a href="#">Projects</a>
        <a href="#">Contact</a>
    </nav>
</header>

<section class="hero">
    <div class="hero-content">
        <h1>Deploy Faster With <span>AWS Elastic Beanstalk</span></h1>

        <p>
            A modern cloud-hosted application running on Python 3.14,
            Flask, and AWS infrastructure.
        </p>

        <a href="#" class="btn">Get Started</a>
    </div>
</section>

<section class="features">
    <div class="card">
        <h3>Fast Deployment</h3>
        <p>Deploy applications quickly with managed infrastructure.</p>
    </div>

    <div class="card">
        <h3>Scalable</h3>
        <p>Automatically scale based on application demand.</p>
    </div>

    <div class="card">
        <h3>Secure</h3>
        <p>Built on AWS security best practices and services.</p>
    </div>
</section>

<footer>
    © 2026 Cloud Application • Powered by AWS Elastic Beanstalk
</footer>

</body>
</html>
"""