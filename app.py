from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Data for individual service pages
services_data = {
    "city-tour": {
        "title": "City Tour",
        "images": [
            {"src": "/static/city 1.JPG",
             "desc": "Dive into the cultural heartbeat of the city with a vibrant art scene."},
            {"src": "/static/IMG_9110.JPG",
             "desc": "Experience the colorful tapestry of local heritage and traditions."},
            {"src": "/static/image.png",
             "desc": "Meet friendly locals and discover hidden gems off the tourist trail."},
            {"src": "/static/IMG_9106.JPG",
             "desc": "Unforgettable moments captured in every corner of the metropolis."},
            {"src": "/static/IMG_9110.JPG", "desc": "Savor exotic cuisine and immerse yourself in the city’s flavors."},
            {"src": "/static/image.png", "desc": "Enjoy guided tours with experts who bring history to life."}
        ],
        "marketing_text": "Ready to explore the city’s beating heart? Our City Tour offers an immersive experience that blends modern vibes with deep-rooted heritage. Book now to embark on an unforgettable journey!"
    },
    "bus-car-hire": {
        "title": "Bus & Car Hire",
        "images": [
            {
                "src": "https://media.istockphoto.com/id/606202170/photo/newlywed-african-couple-sitting-in-the-car.jpg?s=612x612&w=0&k=20&c=S9jCZAIYbQfQ14fiQcOA3bZsDtyMc6u1Xd4dWRJTkxE=",
                "desc": "Weddings: Arrive in style on your special day with our elegant ride."
            },
            {
                "src": "https://thomasalbert.md/wp-content/uploads/2016/04/Airport-Pick-Up.jpg",
                "desc": "Airport Pick Up: Seamless airport transfers for a stress-free start to your journey."
            },
            {
                "src": "https://images.pexels.com/photos/28375913/pexels-photo-28375913/free-photo-of-a-family-in-traditional-clothing-posing-for-a-photo.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "desc": "Family Outing: Perfect for memorable family bonding and adventures."
            },
            {
                "src": "https://images.pexels.com/photos/7464535/pexels-photo-7464535.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "desc": "Group Outing: Spacious, comfortable rides ideal for large groups."
            },
            {
                "src": "https://5.imimg.com/data5/DN/KR/MY-38886318/bus-branding.png",
                "desc": "Advertisement: Transform your vehicle into a dynamic moving billboard."
            },
            {
                "src": "https://www.shutterstock.com/image-photo/back-school-pupils-primary-bus-600nw-1809913087.jpg",
                "desc": "School Excursions: Safe, reliable transport for educational trips."
            }
        ],
        "marketing_text": "Our Bus & Car Hire services are designed to make every journey unforgettable. Whether you're celebrating a wedding, catching a flight, enjoying a family outing, or planning a group adventure, ride with comfort and style. Let us take care of the logistics while you focus on making memories."
    },
    "freight-trucks": {
        "title": "Freight Trucks",
        "images": [
            {
                "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStCofTCeODxVlNAcxj9uQyGvc54CwAQO90Tg&s",
                "desc": "Dry Van Trucking: Keep your cargo secure with our protected solutions."
            },
            {
                "src": "https://i.pinimg.com/736x/8c/11/5e/8c115e5a21cdb998da59bd167af074ee.jpg",
                "desc": "Luggage Movement: Swift, hassle-free transport for personal belongings."
            },
            {
                "src": "https://i.pinimg.com/736x/aa/40/53/aa405323c14ce4aea49f4233a42790b9.jpg",
                "desc": "Specialized Hauling: Heavy-duty trucks built for unique freight requirements."
            },
            {
                "src": "https://i.pinimg.com/736x/44/a2/e8/44a2e865ee767a41333bad33eaf84caa.jpg",
                "desc": "Reefer Trucking: Temperature-controlled solutions for sensitive cargo."
            },
            {
                "src": "https://i.pinimg.com/736x/9c/e9/ae/9ce9aece19444f1bf7a4e7438bbc39a5.jpg",
                "desc": "Equipment Hauling: Safely transport heavy machinery and specialized gear."
            },
            {
                "src": "https://i.pinimg.com/736x/dc/1e/b9/dc1eb9594e49e032cae6302fc7b7eca5.jpg",
                "desc": "Flat Bed Trucking: Versatile solutions for oversize loads."
            }
        ],
        "marketing_text": "Our Freight Truck services are engineered for efficiency and reliability—from dry van trucking to specialized hauling. Count on us to keep your business moving forward with punctual, secure transport solutions."
    }
}

# Main page template
main_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Bus Hire 9ja - Transport & Tour Landing Page</title>
  <!-- Favicon and logo removed -->
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-color: #1FA279;
      --secondary-color: #FBD9C5;
      --dark-color: #333;
      --light-color: #fff;
      --grey-color: #f5f5f5;
      --accent-color: #1FA279;
      --font-size: 1rem;
      --nav-font-size: 0.9rem;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Montserrat', sans-serif;
      color: var(--dark-color);
      background: var(--light-color);
      line-height: 1.5;
    }
    /* Header */
    header {
      width: 100%;
      height: 80vh;
      background: url('https://images.pexels.com/photos/12555019/pexels-photo-12555019.jpeg?auto=compress&cs=tinysrgb&w=1600&h=800') center/cover no-repeat;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      position: relative;
    }
    header::before {
      content: "";
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0,0,0,0.4);
      z-index: 1;
    }
    header .hero-content {
      position: relative;
      z-index: 2;
      color: var(--light-color);
      max-width: 800px;
      padding: 0 1rem;
    }
    header .hero-content h1 { font-size: 2.5rem; margin-bottom: 1rem; }
    header .hero-content p { font-size: 1.1rem; margin-bottom: 1.5rem; }
    header .hero-content a {
      background: var(--primary-color);
      color: var(--light-color);
      text-decoration: none;
      padding: 0.75rem 1.5rem;
      border-radius: 4px;
      font-weight: 600;
    }
    /* Navigation aligned to right */
    nav {
      background: var(--primary-color);
      padding: 1rem;
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }
    nav ul {
      list-style: none;
      display: flex;
      gap: 1rem;
      font-size: var(--nav-font-size);
    }
    nav ul li a {
      color: var(--light-color);
      text-decoration: none;
    }
    nav ul li a:hover { text-decoration: underline; }
    /* Sections */
    section { padding: 2rem 1rem; text-align: center; }
    .why-choose-us, .trip-packages, .reviews, .contact-section {
      background: var(--grey-color);
      margin-top: 1rem;
    }
    .why-choose-us h2, .trip-packages h2, .reviews h2, .contact-section h2 {
      color: var(--primary-color);
      margin-bottom: 2rem;
    }
    /* Grid Layouts */
    .why-grid, .packages-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }
    .why-item, .package-item {
      background: var(--light-color);
      padding: 1rem;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    /* Why Choose Us Icons */
    .why-item img {
      width: 60px;
      height: 60px;
      object-fit: contain;
      margin-bottom: 1rem;
    }
    .why-item h4 {
      color: var(--accent-color);
      margin-bottom: 0.5rem;
      font-size: var(--font-size);
    }
    /* Main Page Services: images fixed at 220×300 */
    .package-item img {
      width: 220px;
      height: 300px;
      object-fit: cover;
      display: block;
      margin: 0 auto;
    }
    .package-content {
      padding: 1rem;
      text-align: center;
    }
    .package-content h3 {
      color: var(--accent-color);
      margin-bottom: 0.5rem;
      font-size: var(--font-size);
    }
    .package-content p { font-size: var(--font-size); margin-bottom: 1rem; }
    .package-content a {
      background: var(--primary-color);
      color: var(--light-color);
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      font-weight: 600;
      font-size: var(--font-size);
    }
    /* Reviews Slider */
    .reviews-slider {
      position: relative;
      max-width: 700px;
      margin: 0 auto;
      overflow: hidden;
    }
    .review-slide {
      display: none;
      padding: 2rem;
      background: var(--light-color);
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .review-slide.active { display: block; }
    .review-slide p { font-style: italic; margin-bottom: 1rem; font-size: var(--font-size); }
    .review-author { font-weight: 700; color: var(--accent-color); font-size: var(--font-size); }
    .slider-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: var(--primary-color);
      color: var(--light-color);
      border: none;
      padding: 0.5rem 1rem;
      cursor: pointer;
      border-radius: 4px;
    }
    .slider-btn.prev { left: 0; }
    .slider-btn.next { right: 0; }
    /* Contact Section */
    .contact-section {
      display: flex;
      flex-wrap: wrap;
      max-width: 1200px;
      margin: 0 auto;
      gap: 2rem;
      padding: 2rem 1rem;
    }
    .contact-left, .contact-right { flex: 1 1 400px; min-width: 300px; }
    .contact-right {
      background: var(--light-color);
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      text-align: center;
    }
    .contact-right form label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: 600;
      font-size: var(--font-size);
    }
    .contact-right form input,
    .contact-right form textarea {
      width: 100%;
      padding: 0.5rem;
      margin-bottom: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: var(--font-size);
    }
    .contact-right form button {
      background: var(--primary-color);
      color: var(--light-color);
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 4px;
      font-weight: 600;
      cursor: pointer;
      font-size: var(--font-size);
    }
    /* Footer */
    footer {
      background: var(--dark-color);
      color: var(--light-color);
      text-align: center;
      padding: 2rem 1rem;
      font-size: var(--font-size);
    }
    footer a {
      color: var(--light-color);
      text-decoration: none;
      margin: 0 0.5rem;
    }
    footer a:hover { text-decoration: underline; }
    /* Responsive tweaks */
    @media (max-width: 768px) {
      header .hero-content h1 { font-size: 2rem; }
      .why-grid, .packages-grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
      .contact-section { flex-direction: column; }
      nav { flex-direction: column; align-items: center; }
    }
  </style>
</head>
<body>
  <!-- Navigation without logo -->
  <nav>
    <ul>
      <li><a href="#hero">Home</a></li>
      <li><a href="#why-choose-us">Why Choose Us</a></li>
      <li><a href="#trip-packages">Services</a></li>
      <li><a href="#reviews">Reviews</a></li>
      <li><a href="#contact-section">Contact</a></li>
    </ul>
  </nav>

  <!-- HERO SECTION -->
  <header id="hero">
    <div class="hero-content">
      <h1>Let's Discover The World Together</h1>
      <p>Explore top-rated tours, reliable transport services, and unbeatable packages for your next adventure.</p>
      <a href="#trip-packages">View Services</a>
    </div>
  </header>

  <!-- WHY CHOOSE US SECTION -->
  <section class="why-choose-us" id="why-choose-us">
    <h2>WHY CHOOSE US?</h2>
    <div class="why-grid">
      <div class="why-item">
        <img src="https://cdn1.iconfinder.com/data/icons/people-tourist-and-family-at-zoo/277/zoo-003-512.png" alt="Expert Guides">
        <h4>Expert Guides</h4>
        <p>Our experienced guides ensure you have the best local knowledge for a memorable trip.</p>
      </div>
      <div class="why-item">
        <img src="https://st2.depositphotos.com/4410397/7488/v/450/depositphotos_74886193-stock-illustration-theater-chairs-icon.jpg" alt="Comfortable Rides">
        <h4>Comfortable Rides</h4>
        <p>Travel in style with modern, well-maintained vehicles and top-notch facilities.</p>
      </div>
      <div class="why-item">
        <img src="https://cdn-icons-png.flaticon.com/512/31/31144.png" alt="Flexible Packages">
        <h4>Flexible Packages</h4>
        <p>Choose from a variety of packages that suit your schedule and budget.</p>
      </div>
      <div class="why-item">
        <img src="https://media.istockphoto.com/id/1353814664/vector/support-customer-24-7-silhouette-icon-help-service-call-center-logo-headphone-with-bubble.jpg?s=612x612&w=0&k=20&c=lLVd-J-OicmgNpHtaI7CU6mMsAyVW60CqD7NnEYyhcQ=" alt="24/7 Support">
        <h4>24/7 Support</h4>
        <p>Our team is here to assist you anytime, ensuring a hassle-free experience.</p>
      </div>
    </div>
  </section>

  <!-- SERVICES SECTION (Main page) -->
  <section class="trip-packages" id="trip-packages">
    <h2>Services</h2>
    <div class="packages-grid">
      <!-- Service 1: City Tour -->
      <div class="package-item">
        <a href="/service/city-tour" target="_blank">
          <img src="https://i.pinimg.com/736x/19/70/85/197085d895ee7eb46fe671a7abdb3675.jpg" alt="City Tour">
        </a>
        <div class="package-content">
          <h3>City Tour</h3>
          <p>Experience the urban landscape with our exclusive city tours.</p>
          <a href="/service/city-tour" target="_blank">Learn More</a>
        </div>
      </div>
      <!-- Service 2: Bus & Car Hire -->
      <div class="package-item">
        <a href="/service/bus-car-hire" target="_blank">
          <img src="https://i.pinimg.com/736x/cd/bb/e8/cdbbe86893b25aa330d9142330d924e2.jpg" alt="Bus & Car Hire">
        </a>
        <div class="package-content">
          <h3>Bus & Car Hire</h3>
          <p>Ride in style on your special day, catch flights with ease, and enjoy memorable outings with loved ones.</p>
          <a href="/service/bus-car-hire" target="_blank">Learn More</a>
        </div>
      </div>
      <!-- Service 3: Freight Trucks -->
      <div class="package-item">
        <a href="/service/freight-trucks" target="_blank">
          <img src="https://static.vecteezy.com/system/resources/previews/035/383/782/non_2x/ai-generated-white-freight-truck-on-gray-background-free-photo.jpg" alt="Freight Trucks">
        </a>
        <div class="package-content">
          <h3>Freight Trucks</h3>
          <p>Efficient logistics with our modern fleet ensuring your cargo is delivered securely.</p>
          <a href="/service/freight-trucks" target="_blank">Learn More</a>
        </div>
      </div>
      <!-- Service 4: Security (Learn More scrolls to contact form) -->
      <div class="package-item">
        <a href="#contact-section">
          <img src="https://i.pinimg.com/474x/e3/e1/9e/e3e19e0d151fa12d24942f112ac387cd.jpg" alt="Security">
        </a>
        <div class="package-content">
          <h3>Security</h3>
          <p>Top-notch security services to ensure safe and secure journeys.</p>
          <a href="#contact-section">Learn More</a>
        </div>
      </div>
    </div>
  </section>

  <!-- REVIEWS SLIDER SECTION -->
  <section class="reviews" id="reviews">
    <h2>Reviews &amp; Testimonial</h2>
    <div class="reviews-slider">
      <div class="review-slide active">
        <p>"Hiring a bus is a big deal for me, but I am glad i did with Bushire9ja. Clean, AC Fitted bus and Professional drivers."</p>
        <span class="review-author">— Jude Chime. Ceo Elan Expo WA.</span>
      </div>
      <div class="review-slide">
        <p>"Exceptional service and friendly staff. I highly recommend their tours and transport services."</p>
        <span class="review-author">— Samantha K(Turkey).</span>
      </div>
      <div class="review-slide">
        <p>"A truly memorable experience. The guides were knowledgeable and the vehicles were top-notch."</p>
        <span class="review-author">— Michael L(Italy).</span>
      </div>
      <div class="review-slide">
        <p>"Reliable, efficient, and professional. Their services exceeded my expectations every time."</p>
        <span class="review-author">— Angela(Wema HR).</span>
      </div>
      <button class="slider-btn prev" onclick="plusSlides(-1)">&#10094;</button>
      <button class="slider-btn next" onclick="plusSlides(1)">&#10095;</button>
    </div>
  </section>

  <!-- CONTACT SECTION -->
  <section class="contact-section" id="contact-section">
    <div class="contact-left">
      <h2>Plan Your Next Travels</h2>
      <p>Ready to start your journey? Contact us today for exclusive offers and personalized packages.</p>
    </div>
    <div class="contact-right">
      <h3>Book Us Now</h3>
      <form method="post" action="/">
        <label for="fullname">Full Name</label>
        <input type="text" id="fullname" name="fullname" required />
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" required />
        <label for="phone">Phone Number</label>
        <input type="text" id="phone" name="phone" required />
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="4"></textarea>
        <button type="submit">Book Now</button>
      </form>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p>© 2025 Bus Hire 9ja. All Rights Reserved.</p>
    <div style="margin-top: 1rem;">
      <a href="https://www.instagram.com/bus.hire9ja?igsh=M2k1dzE2ZnQ4ZDgx" target="_blank">Instagram</a>
    </div>
  </footer>

  <script>
    // Simple slider script for reviews
    let slideIndex = 0;
    const slides = document.getElementsByClassName("review-slide");

    function showSlide(index) {
      if (index >= slides.length) { slideIndex = 0; }
      if (index < 0) { slideIndex = slides.length - 1; }
      for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
      }
      slides[slideIndex].classList.add("active");
    }

    function plusSlides(n) {
      slideIndex += n;
      showSlide(slideIndex);
    }

    // Auto-cycle through slides every 5 seconds
    setInterval(function() { plusSlides(1); }, 5000);
  </script>
</body>
</html>
"""

# Service detail page template for individual service "Learn More" pages
# Here, images are fixed at 300×300
service_page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }} - Bus Hire 9ja</title>
  <!-- Favicon removed -->
  <style>
    :root {
      --primary-color: #1FA279;
      --light-color: #fff;
      --grey-color: #f5f5f5;
      --font-size: 1rem;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { 
      font-family: 'Montserrat', sans-serif; 
      background: var(--grey-color); 
      padding: 2rem; 
      text-align: center; 
    }
    h1 { 
      color: var(--primary-color); 
      margin-bottom: 2rem; 
    }
    .grid-container {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      max-width: 900px;
      margin: 0 auto;
    }
    .grid-item {
      background: var(--light-color);
      border-radius: 8px;
      padding: 1rem;
      box-shadow: 0 0 5px rgba(0,0,0,0.1);
    }
    .grid-item img {
      width: 300px;
      height: 300px;
      object-fit: cover;
      border-radius: 4px;
    }
    .desc {
      margin-top: 0.5rem;
      font-size: var(--font-size);
      color: #444;
    }
    .service-text {
      margin-top: 2rem;
      font-size: var(--font-size);
      color: var(--primary-color);
      max-width: 900px;
      margin: 2rem auto 0;
    }
    a.back {
      display: inline-block;
      margin-top: 2rem;
      text-decoration: none;
      background: var(--primary-color);
      color: var(--light-color);
      padding: 0.5rem 1rem;
      border-radius: 4px;
      font-size: var(--font-size);
    }
  </style>
</head>
<body>
  <h1>{{ title }}</h1>
  <div class="grid-container">
    {% for item in images %}
    <div class="grid-item">
      <img src="{{ item.src }}" alt="Image {{ loop.index }}">
      <div class="desc">{{ item.desc }}</div>
    </div>
    {% endfor %}
  </div>
  <div class="service-text">
    <p>{{ marketing_text }}</p>
  </div>
  <a class="back" href="/">Back to Home</a>
</body>
</html>
"""

# Terms & Conditions / Privacy Policy page (unchanged)
terms_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions / Privacy Policy - Bus Hire 9ja</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Montserrat', sans-serif;
      margin: 2rem;
      line-height: 1.6;
    }
    h1 {
      color: #1FA279;
      text-align: center;
      margin-bottom: 1rem;
    }
    .content {
      max-width: 800px;
      margin: 0 auto;
    }
    a.back {
      display: block;
      text-align: center;
      margin-top: 2rem;
      text-decoration: none;
      background: #1FA279;
      color: #fff;
      padding: 0.5rem 1rem;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <h1>Terms &amp; Conditions / Privacy Policy</h1>
  <div class="content">
    <p>This page outlines the terms and conditions and privacy policy for Bus Hire 9ja. By using our services, you agree to the following terms...</p>
    <!-- Add your detailed T&C and privacy policy content here -->
  </div>
  <a class="back" href="/">Back to Home</a>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        print(f"Received subscription from {fullname} ({email}), Phone: {phone}. Message: {message}")
        return redirect(url_for("home"))
    return render_template_string(main_template)


@app.route("/service/<service_name>")
def service_detail(service_name):
    data = services_data.get(service_name)
    if not data:
        return "Service not found.", 404
    # Use the appropriate template based on service_name if needed.
    # Here, we use the same template for all; images are 300x300.
    return render_template_string(service_page_template,
                                  title=data["title"],
                                  images=data["images"],
                                  marketing_text=data["marketing_text"])


@app.route("/terms")
def terms():
    return render_template_string(terms_template)


if __name__ == "__main__":
    app.run(debug=True)
