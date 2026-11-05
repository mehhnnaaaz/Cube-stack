# CubeStack AI — site content (taken from cubestackai.com) and media references.
FR = "https://framerusercontent.com/images/"
FA = "https://framerusercontent.com/assets/"

def img(i, w=None):
    return FR + i + (f"?width={w}" if w else "")

M = dict(
    logo="1qmBcz9HcW6G3WdVji1K0QYv28s.png",
    icon="snamD3K9VpW2Zkspo95127gFUHI.png",
    hero_bg="5rsUDDMD1tFwNcXO8R03GSRyg.png",
    fisheye="NdRl1vdR3Lk24oRZQ8h6G878M.jpeg",
    retro="Nhg3CzeifKzMzUNXiaWpzJQfbE.jpeg",
    zenith="u0ULoO0mBBntvjAfFRAoyw4GABg.png",
    bhc="DIvxBTXuB9OWFeOPhHQWa6fKg.png",
    shahi="iJIJwEv9IhI08MMpn28bHCrnXI.png",
    group="IUEGTr5CussTQxtdgQ8zMQTd0BA.jpeg",
    couch="7m9DBzdPx9QWNluZid4VdS0UtQ.jpeg",
    book="dalIWC6BHtZSUZn78MDaQG1TDs.jpeg",
    crowd="cG3fVNNYi4Xvl7ncf9D6DmVhQPw.jpg",
    street="KRGbLmA3RSgc8ZhBp2IMJjfU.jpeg",
    phone="8pcVoXaSEYCo5bWV1IGjfargxoo.jpeg",
    adarsh="etsgItJSEmbpGOX5qtcPb5FHS4.png",
    samaksh="cpvSDJPsV72ioMlYEcSEQWwYi4.jpeg",
)
MOTION = ["c2s0Fwt2VQFDMUFpU4VqjqFBNnc.jpg", "daRAPmhTiH99QGs3KpPzXTkEOwI.jpg", "UVdaKaUGZS6moPLaicxxxkmpiI.jpg", "ApXM0Wl2pHcCGMkHAxMN46XhOIM.jpg"]
STEPS = ["HewGZDb4kitchTonXqZWVOG0I.jpeg", "5Gdyi1OlIgjEZyOUJvgHTtiZTY.jpeg", "VmKdVtoi6iwJGNQYKMEQo3J0.jpeg", "MvMpg2CuNUCw6I6d320mlFW2QmY.jpeg"]
AVATARS = ["OmhA69HM1VbnEMV63I5CAKdlNlk.jpg", "nSZJQpCu25uRO9lrT3cjUnyKmk.jpg", "UY6B0qS4hdcjlEgPYtxTooD5yA.jpg", "q73UUTq2vptjoL40m0slx7bgMOo.jpg", "9Y0nJrgRCo37O08gSitLgIUGDg.jpg"]
V_EARTH = FA + "5adilcsalaKdxxagnYNl6Sbx58c.mp4"
V_TREES = FA + "CTtqK8nDBlY43FXLsMwN2T1EAXI.mp4"
V_RIBBON = FA + "ab5DhkLnHv3W40wSSIOQuICoY.mp4"

PHONE_MAIN = "+91 95772 97297"
PHONE_MAIN_RAW = "+919577297297"
WA_MAIN = "https://wa.me/919577297297"
WA_ACCESS = "https://wa.me/919599993737"   # number used by the "Request Access" button on the live site
EMAIL = "admin@cubestackai.com"
ADDRESS = ["Ground Floor, PP Towers", "Plot No. C-1, 2 &amp; 3, Netaji Subhash Place", "Pitampura, New Delhi, Delhi 110034"]
IG = "https://www.instagram.com/cubestackai/"
LI = "https://www.linkedin.com/company/cubestackai/"

SERVICES = [
    dict(word="Rank high", title="Local Search Dominance",
         text="We analyse your entire local presence — Google rankings, GBP health, competitor gaps, and review standing — then build and execute a precise growth roadmap that gets you ranking where it counts.",
         incl=["GBP audit", "Competitor gap map", "Keyword opportunity report"]),
    dict(word="Earn trust", title="GBP &amp; Reputation Management",
         text="We fully manage your Google Business Profile — daily posts, photo strategy, Q&amp;A, and AI-powered replies to every review — so your profile works as a 24/7 sales asset.",
         incl=["Weekly GBP posts", "AI review replies", "Reputation monitoring"]),
    dict(word="Own local", title="Local SEO &amp; Visibility Engine",
         text="We build your local search dominance through keyword clustering, geo-tagging, citation management, and on-page optimisation — engineered to rank you where your customers are searching.",
         incl=["Keyword clustering", "Geo-tagging", "Monthly ranking report"]),
    dict(word="Stay top", title="Conversion Funnels &amp; Growth Systems",
         text="We design the full customer journey — from first click to booked inquiry. Landing pages, digital booklets, feedback intelligence, and authority content that turns visibility into revenue.",
         incl=["Custom landing pages", "Digital booklets", "Feedback intelligence system"]),
]

WHY = [
    ("Data first, always.", "Every decision we make is backed by search data, ranking intelligence, and real customer behaviour. Never guesswork."),
    ("Your city. Your #1.", "We engineer your presence to dominate your neighbourhood, your category, and your keyword — where your customers are actually searching."),
    ("Ranked before your competition.", "Websites are built lightning-fast, SEO-ready, and crafted for higher ranking visibility online."),
    ("Reputation that sells.", "Your reviews, rating, and Google profile become your most powerful sales tool. We manage every inch of it daily."),
    ("Inside your growth loop.", "We don't send monthly reports and disappear. We are embedded in your business — tracking, optimising, and pushing performance every single day."),
]

SECTORS = [
    ("Restaurants &amp; Cafes", "More reservations &amp; walk-ins", "Rank #1 on local search &amp; maps"),
    ("Clinics &amp; Dentists", "More booked appointments", "GBP management &amp; trust building"),
    ("Hotels &amp; Hospitality", "More direct bookings", "Reputation engine &amp; review growth"),
    ("Salons &amp; Wellness", "More repeat clients", "AI reviews &amp; reputation management"),
    ("Auto Services", "More service bookings", "GBP + local pack ranking"),
]

FAQ = [
    ("How long does it take to see results?", "Most clients start seeing movement in their Google rankings and profile visibility within the first 30 to 45 days. Significant ranking improvements and a measurable increase in inquiries typically happen between 60 and 90 days. Local SEO is not overnight — but once the system kicks in, it compounds every single month."),
    ("We already have a Google Business Profile. Do we still need this?", "Having a GBP and having an optimised, actively managed GBP are two very different things. Most businesses set it up once and never touch it again. We manage it daily — posts, photos, Q&amp;A, review replies, category updates — turning it from a dormant listing into your most powerful customer acquisition tool."),
    ("How is CubeStack different from a regular SEO agency?", "Most SEO agencies focus on your website. We focus on your entire local digital presence — your Google ranking, your reputation, your reviews, and your conversion funnel all working together as one system. We don't send you a report at the end of the month and disappear. We are inside your growth loop every single day."),
    ("What kind of businesses do you work with?", "We work with local businesses that depend on customers finding them online — restaurants, clinics, law firms, hotels, salons, retail shops, auto services, and consultants. If your business serves a local area and needs more calls, bookings, or walk-ins, we are built for you."),
    ("What happens to our rankings if we stop working with you?", "The infrastructure we build — your optimised GBP, your review volume, your local citations, your keyword rankings — stays with you. Rankings don't disappear overnight. However, like any growth system, consistent management is what keeps you at the top. The moment you stop, competitors who are actively investing will start closing the gap."),
]

TEAM = [
    dict(name="Adarsh Ghai", role="CEO &amp; Founder", city="Delhi", img=M["adarsh"],
         ig="https://www.instagram.com/adarshghaii/", li="https://www.linkedin.com/in/adarsh-ghai-a7b329139/"),
    dict(name="Samaksh Kalra", role="CMO", city="Delhi", img=M["samaksh"],
         ig="https://www.instagram.com/samakshkalraa/", li="https://www.linkedin.com/in/samaksh-raghav-kalra-6a9b48137/"),
]

TESTIMONIALS = [
    dict(name="Dr Vijay Singhal", org="Dermatologist · South Delhi", img="rPgmrSM3CD2pF9PuJYCwRzLtes.jpg",
         text="We went from invisible to #1 for “best dermatologist in South Delhi” in under 60 days. Appointment bookings doubled. Patients now walk in specifically because they found us on Google and trusted our reviews. CubeStack didn't just improve our ranking — they built our reputation online."),
    dict(name="Dr Mayuri Jain", org="Skin DNA Clinic · Delhi", img="KjQkOyGM1Lc7Vko9MaaAutEtcuI.webp",
         text="Delhi has hundreds of dermatology clinics. Standing out felt impossible until CubeStack rebuilt our entire Google presence from scratch. They optimised our profile, managed our reviews with their AI system, and targeted the exact keywords our patients were searching — PRP treatment Delhi, skin specialist South Delhi, hair loss treatment. Within 75 days we were ranking in the top 3 for every single one."),
    dict(name="Dr Ghanim", org="Shahi Manjil · Toronto", img="f1TY28Vt93iiezG6xmtkNI5kc.webp",
         text="Before partnering with CubeStack AI, our real-world reputation in Toronto was outstanding, boasting a 4.8-star rating from thousands of loyal guests. However, our digital infrastructure didn't reflect that success. Our Google profile suffered from a severe business name violation that risked suspension, we had zero active Google Posts, our service depth was completely unpopulated, and we lacked a direct booking link to convert searching diners. We were practically invisible to the modern AI search tools and Map Packs where today's diners make decisions."),
]

CASES = [
    dict(
        slug="zenith-skin-hair-dental-clinic-punjabi-bagh",
        name="Zenith Skin, Hair &amp; Dental Clinic", short="Zenith",
        title="Zenith Skin, Hair &amp; Dental Clinic — Multi-Specialty Clinic in Punjabi Bagh, West Delhi",
        kind="Multi-specialty clinic", area="Punjabi Bagh, West Delhi",
        tags=["2026", "AEO", "Google Business Profile Management"],
        category="AEO | Google Business Profile Management", year="2026",
        client="Dr. Aparna Singhal &amp; Dr. Vijay Singhal — Zenith Skin, Hair &amp; Dental Clinic", location="Delhi | India",
        live="https://share.google/SeVrcPgV9BWMqnE9k",
        hero="n8ifxhG02KH7qGMhLHEi60Q54.png", card=M["zenith"],
        overview=[
            "Zenith Skin, Hair &amp; Dental Clinic operates from Punjabi Bagh West — one of the busiest healthcare belts in West Delhi, sitting on the Ring Road corridor that connects Punjabi Bagh to Rajouri Garden, Tagore Garden, and Paschim Vihar. The clinic runs three active specialties under one roof: a dermatology and aesthetics department, a trichology and hair restoration unit, and a full-service dental practice.",
            "Despite years of strong clinical delivery, the Google Business Profile painted a different picture. The audit found a profile that had been built for skin alone — the primary category, description, services, and all keyword signals were concentrated in dermatology. Hair and dental were virtually invisible on Google, with no dedicated service entries, no keyword targeting, and no category coverage. For a clinic whose growth plan depends on cross-specialty patient acquisition, this was a structural problem, not a performance problem.",
        ],
        headline="Skin ranked. Hair and dental were invisible.",
        pull="The gap for Zenith was not clinical, it was infrastructure. The skin vertical was competitive. Hair and dental needed to be built from scratch on Google.",
        approach="We opened with a full 5-pillar GBP audit — Relevance, Prominence, Profile Completeness, Photos, and Conversion — scoring Zenith's profile and identifying the root blocking issues across all three verticals. The audit produced a prioritised fix list. We executed in three phases.",
        phases=[
            ("Phase 1 — Multi-Specialty Profile Rebuild", [
                "Reconfigured the primary GBP category to 'Dermatologist' — retaining skin dominance while opening the profile to multi-specialty keyword justification",
                "Added 8 secondary categories spanning Skin Care Clinic, Hair Transplant Surgeon, Hair Loss Treatment Clinic, Dental Clinic, Cosmetic Dentist, Laser Hair Removal Service, Medical Spa, and Beauty Salon",
                "Rewrote the 750-character business description to cover all three verticals — 'Best skin, hair &amp; dental clinic in Punjabi Bagh' in sentence one, with West Delhi and Punjabi Bagh geo-signals embedded across all three specialty mentions",
                "NAP consistency audit and correction across Justdial, Practo, Sulekha, and IndiaMart — aligning name, address, and phone exactly across all platforms",
                "Added 3 dedicated opening hours entries per specialty where applicable, and corrected appointment booking link to direct URL",
                "Uploaded 20+ geo-tagged photos across all three departments — clinic exterior, reception, skin treatment rooms, hair treatment chairs, dental chairs, and doctor portraits",
            ]),
            ("Phase 2 — Three-Vertical Service Catalogue (45 entries)", [
                "Built a 15-entry skin services catalogue — each entry with a geo-targeted description seeded with Punjabi Bagh, West Delhi, and nearby neighbourhood signals (Rajouri Garden, Tagore Garden, Paschim Vihar)",
                "Built a 15-entry hair services catalogue — covering PRP, GFC, mesotherapy, hair transplant consultation, alopecia treatment, and scalp analysis, each geo-targeted to Punjabi Bagh and surrounding West Delhi catchment",
                "Built a 15-entry dental services catalogue — covering Invisalign, teeth whitening, dental implants, smile makeover, root canal, braces, and paediatric dentistry with West Delhi geo-signals embedded",
                "Seeded 15 keyword-rich Q&amp;A pairs across Google GBP Q&amp;A — 5 per specialty — covering the clinic's highest-intent patient search queries",
            ]),
            ("Phase 3 — Social Proof &amp; Authority Engine", [
                "Launched the Zenith Review Programme — QR codes placed at 3 touchpoints per department (reception, treatment room, checkout desk) directing patients to Google review after each visit",
                "WhatsApp review request scripts activated within 2 hours of each appointment — one version per specialty with condition-specific language",
                "AI review response bot activated — every Google review replied to within 2 hours with personalised responses referencing the specific treatment and department",
                "Google Posts published 2x per week across all three specialty themes — targeting 'Best dermatologist Punjabi Bagh', 'Hair loss treatment West Delhi', and 'Dentist near me Punjabi Bagh' in rotation",
                "Monthly keyword ranking and profile performance report delivered — tracking position movement, call clicks, and direction requests per specialty",
            ]),
        ],
        results=[
            "The category rebuild and multi-specialty service catalogue triggered ranking movement within 7 days of deployment. The profile — which had previously registered almost no impressions for hair or dental search terms — began appearing in the West Delhi local pack for 'PRP hair treatment Punjabi Bagh', 'hair loss treatment West Delhi', 'dentist Punjabi Bagh', and 'Invisalign West Delhi' within the first 30 days. The secondary category additions gave Google the signal justification needed to associate the profile with all three specialty verticals simultaneously.",
            "The 45-entry product catalogue — 15 per specialty — became the primary keyword justification engine. Each entry contributed geo-targeted relevance signals across Punjabi Bagh, Rajouri Garden, Tagore Garden, and Paschim Vihar. The review velocity programme began generating consistent new reviews within the first 2 weeks, with patients leaving condition-specific language that Google's algorithm used to validate the specialty categorisation. New patients arriving via Google began self-identifying which department brought them — the first time Zenith had measurable multi-channel attribution from organic search.",
        ],
        stats=[("Top 3", "Ranked on Google Maps for target skin, hair &amp; dental keywords in West Delhi"),
               ("3x", "Verticals ranked — skin, hair, and dental each hitting local pack"),
               ("4.8★", "Target Google rating — sustained with AI review management across all 3 specialties")],
        quote="Punjabi Bagh is one of West Delhi's most competitive healthcare corridors — dozens of skin clinics, hair clinics, and dental practices all chasing the same patients. Before CubeStack, our Google presence reflected none of the work we'd built across three specialties. Skin was holding its own, but hair and dental were practically invisible. CubeStack came in with a structured audit, fixed what was broken at the foundation level, and built out a complete content and review infrastructure across all three verticals. Within 45 days, we were ranking in the top 3 for key hair and dental terms we'd never appeared for before. The AI review response system means every patient gets acknowledged within hours, which has genuinely changed how new patients feel about us before they've even walked in.",
        quote_name="Dr. Vijay Singhal", quote_role="MBBS, MD — Dermatology · Founder &amp; Lead Consultant, Zenith Skin, Hair &amp; Dental Clinic",
        quote_img="rPgmrSM3CD2pF9PuJYCwRzLtes.jpg",
        gallery=["XvYWouKw5d9zsg97WQNo7PkVCOI.jpeg", "Skd2Tlj5KyBRuGhsQk6MbFXrNE.jpeg", "cNK3MPGUoTTg6S0qD1x6VmzWfc.png", "Jr5EXKsamzIihBg7Zl9W63ykonA.jpeg", "8izOb2wbxHruPflZtBc8z2oE9II.jpeg", "sHCPte5ea2rNuZYSbEYVpJ5AE.png", "xPHB8xgfHlPrMwDN9MDjjoeIPg.png", "C88hp0ZHh6P5hBkW2pr079eLh4k.png", "vsHtOU2OQEkhICne1Kh9CUVUj2E.png", "Ja3NW6bstFY34aYJdyMf8TJoK2c.png", "nQuHKaJfJ7Lzv3gyRLmAvwKgA4.png"],
    ),
    dict(
        slug="bhc-wellness-diagnostic-centre-pitampura-delhi",
        name="BHC Wellness", short="BHC",
        title="BHC Wellness — Diagnostic &amp; Wellness Centre in Pitampura, Delhi",
        kind="Diagnostic &amp; wellness centre", area="Pitampura, Delhi",
        tags=["2026", "GBP Management", "AEO"],
        category="Google Business Profile Management &amp; AEO", year="2026",
        client="Mr. Tanuj Kalra | MD", location="Pitampura | North Delhi, India",
        live="https://maps.app.goo.gl/9hzHceDTD9AexiPh6",
        hero=M["bhc"], card=M["bhc"],
        overview=[
            "BHC Wellness operates from 196 Sainik Vihar, Pitampura — near Rani Bagh Market and Apeejay School, in one of North Delhi's busiest mixed-residential and commercial corridors. The centre runs a comprehensive wellness and diagnostics operation covering general wellness health packages, condition-specific checkups, women's and maternal health programmes, bone, joint, and spine packages, physiotherapy and acupuncture, nutrition and weight management, and a full-service pathology and radiology laboratory.",
            "Despite a broad service offering and competitive pricing — packages ranging from Rs. 599 to Rs. 4,299 — the Google Business Profile was not converting that offering into visibility. The profile had incomplete categorisation, no product catalogue, sparse photo coverage, and a review velocity near zero. Pitampura's diagnostic and wellness market is competed by established players with strong Maps presence.",
            "The GBP audit identified the primary category as too generic, no secondary categories covering physio or nutrition specialisms, a business description that gave Google no keyword justification signals, and no active review collection mechanism for a centre processing patients daily across multiple departments.",
        ],
        headline="A broad offering. Near-zero visibility.",
        pull="The gap for BHC Wellness was not clinical — it was infrastructure.",
        approach="We opened with a full 5-pillar GBP audit — Relevance, Prominence, Profile Completeness, Photos, and Conversion — scoring the profile and mapping every gap against the catchment area's competitive landscape. Execution ran in three phases.",
        phases=[
            ("Phase 1 — Profile Foundation Rebuild", [
                "Set primary GBP category to 'Medical Diagnostic Imaging Center' with 6 secondary categories covering Wellness Centre, Physiotherapy Center, Nutritionist, Medical Laboratory, Women's Health Clinic, and Weight Loss Service",
                "Rewrote 750-character business description opening with 'Best wellness and diagnostic centre in Pitampura' — Pitampura, Sainik Vihar, and Rani Bagh geo-signals embedded across all specialty mentions",
                "NAP consistency corrected across Justdial, Practo, Sulekha, and IndiaMart — name, address, and phone aligned exactly across all listings",
                "Corrected appointment booking link to bhcwellness.in and verified hours: Mon–Sat 8 AM–8 PM, Sunday 8 AM–2 PM",
                "Uploaded 20+ geo-tagged photos across all departments — exterior, reception, pathology lab, physio room, wellness consultation area, and diagnostic equipment",
            ]),
            ("Phase 2 — Full Wellness &amp; Diagnostics Product Catalogue (30+ entries)", [
                "Built a 10-entry General Wellness Packages catalogue — descriptions geo-tagged to Pitampura, Rani Bagh, Rohini, Shalimar Bagh, Ashok Vihar, and Kohat Enclave",
                "Built a 6-entry Condition-Specific Checkups catalogue — diabetes, thyroid, cardiac, kidney, liver, and full body — each with geo-tagged, GBP-compliant descriptions",
                "Built a 5-entry Women's &amp; Maternal Health catalogue — covering antenatal, PCOD, gynaecology, and menopause packages",
                "Built a 5-entry Physio, Bone &amp; Lifestyle catalogue — bone/joint/spine (basic and advanced), obesity management, and weight gain packages",
                "Built a 5-entry Pathology &amp; Radiology catalogue covering microbiology, haematology, biochemistry, digital X-ray, and ECG/echo diagnostic entries",
                "Seeded 10 keyword-rich Q&amp;A pairs covering the centre's highest-intent patient searches across wellness, diagnostics, and physio",
            ]),
            ("Phase 3 — Review Velocity &amp; Authority", [
                "Launched BHC Review Programme — QR codes at reception, pathology collection window, and physio exit — routing 4–5 star responses to Google Reviews, 1–3 stars to private feedback form",
                "Custom CubeStack feedback landing page (bhcwellness review funnel) with department-specific routing — Paediatric, Physio, Pharmacy, Skin &amp; Cosmetic Surgery",
                "WhatsApp review request script deployed post-appointment with department-specific copy variants",
                "AI review response bot activated — every Google review responded to within 2 hours with personalised, professionally worded replies",
                "Google Posts published 2x per week covering wellness package offers, diagnostic service highlights, and seasonal health tips — all geo-tagged to Pitampura and surrounding North Delhi areas",
                "Monthly ranking and profile performance report tracking call clicks, direction requests, and keyword position movement",
            ]),
        ],
        results=[
            "The primary category fix and product catalogue deployment triggered ranking movement within 7 days. The profile — which had generated near-zero impressions for wellness and diagnostic search terms — began appearing in the local pack for 'wellness centre Pitampura', 'health checkup packages Pitampura', 'physiotherapy Pitampura', and 'diagnostic centre near Rani Bagh' within the first 30 days. The 30+ entry product catalogue became the primary keyword justification engine, with each geo-tagged description contributing Pitampura, Shalimar Bagh, Rohini, and Ashok Vihar relevance signals that Google's algorithm used to validate the categorisation.",
            "The review velocity programme began generating consistent new reviews within the first 2 weeks of activation. The QR funnel at reception — routing satisfied patients directly to Google Reviews — proved to be the single highest-converting patient touchpoint the centre had operated. The AI response bot ensured 100% review coverage, a trust signal that measurably influenced new patient decisions. Patients began arriving citing the Google rating specifically — the first measurable evidence of Google-first patient acquisition for BHC Wellness.",
        ],
        stats=[("Top 3", "Ranked on Google Maps for wellness and diagnostic searches across Pitampura and North Delhi"),
               ("30D", "Time to first measurable ranking movement after profile rebuild"),
               ("4.8★", "Target Google rating sustained with AI-managed review responses across all departments")],
        quote="Pitampura is a densely competitive diagnostic and wellness corridor — patients have dozens of options within walking distance. When we opened, our Google presence was essentially zero. CubeStack rebuilt our profile from the ground up, structured our product catalogue across all our wellness packages, and launched the review programme that started generating consistent patient feedback within the first two weeks. Within 30 days we were appearing in the local pack for wellness and diagnostic searches across Pitampura, Rani Bagh, Rohini, and Shalimar Bagh. The AI review response system means every patient gets a professional, personalised reply within hours — that has genuinely changed how new patients perceive us before they walk in.",
        quote_name="Tanuj Kalra", quote_role="Founder, Bhritii Health Care", quote_img="sAmm5Co033g7aUf2hlQhHumHVs0.png",
        gallery=["vepFr5QsbXo0kRe2FI1t9jwFFaQ.png", "0n669yno8w4SG2UEetaD4WsJcbs.png", "eiykiwuHMhbqGWBRlc3BPV6fTrA.png", "9fP0g3STWATCSjZ8yxTPXdaaxIE.png", "pjYmpCykTPWTac9obzNo0EezCNk.png", "4KU9wNDLRsIURfTQz9GgBi85o.png", "eAkC3W7k0KT7Avr3bkA6sZJso8.png", "FuAaflhsHPdahPSixeGJ8N0mH8.png", "r2KhN7UzuBYKwyZo1CkT13yXA5g.png", "Z3olUknyJKrDYKaHTjMHnfbAsQ.png"],
    ),
    dict(
        slug="shahi-manjil-north-york",
        name="Shahi Manjil", short="Shahi",
        title="Shahi Manjil — Fine Dining Indian Restaurant in North York, Toronto",
        kind="Fine-dining Indian restaurant", area="North York, Toronto",
        tags=["2026", "AEO", "GBP Management", "GEO"],
        category="AEO | Google Business Profile Management | GEO", year="2026",
        client="Shahi Manjil", location="Toronto | Canada",
        live="https://share.google/7WkOqRz33Pkv0VK53",
        hero=M["shahi"], card=M["shahi"],
        overview=[
            "Shahi Manjil operates from a premium location at 3820 Victoria Park Ave in North York, Toronto, serving a dense culinary catchment area that spans North York, Scarborough, Markham, and the broader Greater Toronto Area (GTA). Spearheaded by four specialist regional chefs operating a strict policy of using no MSG or artificial colors, the restaurant delivers authentic Indian fine dining.",
            "Despite boasting an elite 4.8-star review base, a comprehensive digital audit uncovered significant technical and operational visibility gaps. The profile suffered from a severe business name guideline violation (creating a high suspension risk), zero active Google Posts engagement, unpopulated Services and Q&amp;A fields, and a total lack of structured booking deep links to convert high-intent maps traffic. This resulted in an overall GBP Score of just 58/100, causing a severe 'Visibility Gap' across traditional maps and conversational AI search engines.",
        ],
        headline="4.8 stars. A profile score of 58/100.",
        pull="An elite 4.8-star review base, held back by compliance and visibility gaps across maps and conversational AI search.",
        approach="We executed a targeted 30-day structural visibility framework designed to fix foundational operational elements, build real-time social proof, and optimize the brand for modern AI-driven Search/Generative Engine Optimization (SEO/GEO).",
        phases=[
            ("Phase 1 — Foundational Profile &amp; Compliance Rebuild", [
                "Guideline Compliance Cleanup: Trimmed the business name from its keyword-stuffed variation down to the compliant storefront name: 'Shahi Manjil' to eliminate profile suspension risks",
                "Conversion Streamlining: Integrated direct booking and order URLs inside the profile dashboard, linking OpenTable to eliminate conversion friction.",
                "Category Restructuring: Locked in 'Indian Restaurant' as the verified primary category and added four rich secondary categories (Fine Dining Restaurant, Catering Food and Drink Supplier, Event Venue, and South Asian Restaurant).",
                "Search Engine Optimization (SEO) Copywriting: Deployed a geo-tagged, paste-ready 750-character business description utilizing organic high-intent keywords within the first 100 characters",
            ]),
            ("Phase 2 — Three-Vertical Service &amp; Query Catalog", [
                "15-Entry Service Grid: Built and deployed 15 fully optimized, geo-targeted custom service items (e.g., Indian Catering Services Toronto, Halal Indian Restaurant, Biryani Restaurant Toronto) to populate Google's search justification snippets.",
                "Authority Seeded Q&amp;A: Programmed and deployed 5 strategic community question-and-answer pairs addressing parking accessibility, vegetarian parameters, large group configurations, and signature dish entries.",
            ]),
            ("Phase 3 — Social Proof &amp; Authority Engine", [
                "Structured Content Cadence: Implemented a consistent post schedule of 3 update/offer assets per week, indexing active search phrases like \"Best Indian Restaurant Toronto\".",
                "Review Infrastructure Calibration: Implemented a comprehensive review tracking and structured response strategy using specialized sentiment templates to maximize local engagement metrics.",
                "Advanced AI Schema Architecture: Injected custom LocalBusiness JSON-LD schema code directly into the brand's core domain framework, defining geographic variables, pricing indexes, and exact coordinates so AI models (ChatGPT, Gemini, and Apple Maps) can accurately cross-reference and recommend the business entity",
            ]),
        ],
        results=[
            "The comprehensive optimization track successfully transitions Shahi Manjil from the 'Struggling' index to a 'Dominant' tier-one local profile. Remediation of the business name violation eliminated immediate compliance vulnerabilities, while the integration of the direct OpenTable tracking link captured leaking consumer intent directly from search maps.",
            "Within 30 to 60 days of deployment, the expansion of the 15-entry keyword service grid triggers active 'justification snippets' beneath regional search queries. The implementation of structured JSON-LD schema feeds clean, authoritative entity data points directly to AI scrapers. This resolves the visibility gap, successfully establishing Shahi Manjil as an authoritative, trusted entity frequently cited in conversational AI search summaries and locked into top-tier Local Map Pack tracking metrics.",
        ],
        stats=[("Top 3", "Projected Google Maps Local Pack placement for highly competitive target keywords within 60 days."),
               ("58→80+", "Scaling the overall Google Business Profile health score from the struggling tier to a dominant market presence"),
               ("4.8★", "Sustaining an exceptional, authentic rating across more than 4,300 structural community reviews.")],
        quote="Our authentic fine dining restaurant possessed an incredible real-world foundation with a 4.8-star rating and thousands of loyal guests, yet our online footprint was completely restricted by an unoptimized Google Business Profile. Critical visibility gaps like zero active Google Posts, an incomplete services depth, a policy-violating business name, and a missing direct booking link kept us hidden from top-tier local maps results. CubeStack built an intentional, multi-phase digital infrastructure that safely brought us into complete compliance. They populated a 15-entry keyword-optimized service catalog, activated missing conversion points to directly link our OpenTable reservation system, and established consistent publishing cadences. Within weeks, our visibility signals fundamentally changed, establishing Shahi Manjil as a trusted entity that AI search tools and maps systems seamlessly recommend to high-intent diners across Toronto.",
        quote_name="Dr Ghani", quote_role="Owner, Shahi Manjil", quote_img="f1TY28Vt93iiezG6xmtkNI5kc.webp",
        gallery=["iSAL2IX7QAaZxnIbt4YTYHLJfk.png", "lKXUr9GOcwpbGahSO7m9FqDA3s.png", "TgUiXTOT9n0TWWZtKEANwKPwUE.png", "UzNb95HP5cWrbJdxFxhzKqZ9k.png", "cVC6MfYWslCkniTStuGHCn3dg.png", "YOFnO9zNH3A16SqNYcNV2aHxB4.png", "OkY5q880dDeatvNmkAqVQLwS1uY.png", "PzeUTikhWDqqjUIhWWUOXVxLJ0.png", "aMS6M2j5Ti3kj6qn8G8RoRweX0.png", "FJBV8NkSyq35fRwvaYbhkZiLRk.png", "NPYTEkhnMorNwO3M2uhIRdhCGk4.jpeg"],
    ),
]

PRIVACY = [
    ("1. Who we are", ["CubeStack AI is a local business growth partner that provides search optimization, Google Business Profile management, AI-powered review management, and conversion funnel services. When you use our website or engage our services, you are trusting us with your information. We take that seriously.",
                       "Company name: CubeStack AI · Contact email: admin@cubestackai.com · Website: cubestackai.com"], []),
    ("2. What information we collect", ["<b>Information you give us directly:</b>"], ["Full name and business name", "Email address and phone number", "Business type, location, and website URL", "Any information submitted through our contact forms, audit requests, or onboarding documents"]),
    ("", ["<b>Information we collect automatically:</b>"], ["IP address and browser type", "Pages visited and time spent on our website", "Device type and operating system", "Referral source — how you found our website"]),
    ("", ["<b>Information from third parties:</b>"], ["Google Business Profile data when you grant us management access", "Review platforms and local directory data relevant to your business", "Analytics data from tools like Google Analytics"]),
    ("3. How we use your information", ["We use the information we collect to:"], ["Deliver our services — managing your GBP, local SEO, review responses, and conversion systems", "Communicate with you about your account, results, and recommendations", "Send you performance reports and growth updates", "Respond to your enquiries and support requests", "Improve our services and internal processes", "Send you relevant insights and growth tips if you have opted in", "Comply with legal obligations"]),
    ("", ["We will never sell your personal information to third parties. Ever."], []),
    ("4. How we share your information", ["We only share your information in the following circumstances:",
        "<b>Service providers:</b> We work with trusted third-party tools and platforms — including Google, scheduling software, analytics platforms, and communication tools — to deliver our services. These providers only access your data to the extent necessary to perform their function.",
        "<b>Legal requirements:</b> We may disclose your information if required by law, court order, or government authority.",
        "<b>Business transfers:</b> If CubeStack AI is acquired or merges with another company, your information may be transferred as part of that transaction. You will be notified in advance.",
        "We do not sell, rent, or trade your personal information to any third party for marketing purposes."], []),
    ("5. Google Business Profile access", ["When you onboard with CubeStack AI and grant us access to your Google Business Profile, we use that access exclusively to manage and optimise your profile on your behalf. This includes posting updates, responding to reviews, updating business information, and monitoring performance. We do not use your GBP access for any purpose beyond delivering your agreed services."], []),
    ("6. Data retention", ["We retain your personal information for as long as you are an active client and for a reasonable period after your engagement ends — typically 12 months — unless a longer retention period is required by law. After this period your data is securely deleted or anonymised."], []),
    ("7. Your rights", ["Depending on your location you may have the following rights regarding your personal data:"], ["The right to access the personal information we hold about you", "The right to correct inaccurate or incomplete information", "The right to request deletion of your personal information", "The right to restrict or object to how we process your data", "The right to data portability — receiving your data in a usable format", "The right to withdraw consent at any time where processing is based on consent"]),
    ("", ["To exercise any of these rights please contact us at admin@cubestackai.com. We will respond within 30 days."], []),
    ("8. Cookies", ["Our website uses cookies to improve your browsing experience and analyse how visitors use our site. Cookies are small text files stored on your device.", "We use the following types of cookies:"], ["Essential cookies — necessary for the website to function", "Analytics cookies — help us understand how visitors interact with our site", "Marketing cookies — used to track visits and measure the effectiveness of our campaigns"]),
    ("", ["You can control cookie preferences through your browser settings at any time. Disabling certain cookies may affect the functionality of our website."], []),
    ("9. Third party links", ["Our website may contain links to third party websites including Google, social media platforms, and partner tools. We are not responsible for the privacy practices of those websites and encourage you to read their privacy policies independently."], []),
    ("10. Children's privacy", ["Our services are intended for business owners and professionals. We do not knowingly collect personal information from anyone under the age of 18. If you believe a minor has provided us with personal information please contact us immediately."], []),
    ("11. Security", ["We take reasonable technical and organisational measures to protect your personal information against unauthorised access, loss, alteration, or disclosure. These measures include secure data storage, encrypted communications, and restricted access controls. However no method of transmission over the internet is 100% secure and we cannot guarantee absolute security."], []),
    ("12. Changes to this policy", ["We may update this privacy policy from time to time to reflect changes in our practices or legal requirements. When we make significant changes we will notify you by email or by posting a prominent notice on our website. The date at the top of this policy reflects when it was last updated."], []),
    ("13. Contact us", ["If you have any questions, concerns, or requests regarding this privacy policy or how we handle your data please contact us:", "CubeStack AI · Email: admin@cubestackai.com · Website: cubestackai.com", "We are committed to resolving any privacy concerns promptly and transparently."], []),
]
