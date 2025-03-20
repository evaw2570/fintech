import streamlit as st
import pandas as pd
import pydeck as pdk

# Page configuration
st.set_page_config(page_title="Global Financial Regulations Hub", layout="wide")

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import plotly.express as px

import streamlit as st
import plotly.express as px
import pandas as pd

import streamlit as st
import plotly.express as px
import pandas as pd

# Custom CSS for styling
st.markdown("""
<style>
    .feature-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 10px;
        text-align: center;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    .pricing-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    .pricing-table th, .pricing-table td {
        padding: 15px;
        text-align: center;
        border: 1px solid #ddd;
    }
    .pricing-table th {
        background-color: #f4f4f4;
    }
    .footer {
        margin-top: 50px;
        padding: 20px;
        background-color: #f4f4f4;
        text-align: center;
    }
    /* Custom Button Styles */
    .custom-button {
        background-color: #e6a8d7; /* Light Purple */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .custom-button:hover {
        background-color: #d291bc; /* Darker Purple on Hover */
    }
    .header {
            background: linear-gradient(135deg, #4a1c61, #6a2c91);
            color: white;
            padding: 1rem;
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            border-radius: 10px;
    }
    .subheader {
            text-align: center;
            font-size: 1.5rem;
            color: #4a1c61;
            margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>🌍 Global Financial Regulations Hub</div>", unsafe_allow_html=True)

# Sample regulatory updates - moved to global scope with representative images
updates = [
    {"Region": "USA", "Update": "SEC Finalizes New Climate Disclosure Rules", "Date": "March 15, 2025", 
     "Image": "https://images.unsplash.com/photo-1621944190310-e3cca1564bd7?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Securities and Exchange Commission has finalized rules requiring public companies to disclose climate-related financial risks."},
    
    {"Region": "EU", "Update": "ECB Updates Digital Euro Framework", "Date": "March 12, 2025", 
     "Image": "https://images.unsplash.com/photo-1580674285054-bed31e145f59?w=800&h=600&fit=crop&auto=format", 
     "Description": "The European Central Bank has released a comprehensive framework for the implementation of the Digital Euro."},
    
    {"Region": "UK", "Update": "FCA Introduces Enhanced Consumer Protection Rules", "Date": "March 10, 2025", 
     "Image": "https://images.unsplash.com/photo-1486299267070-83823f5448dd?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Financial Conduct Authority has implemented new rules to strengthen consumer protection in financial services."},
    
    {"Region": "China", "Update": "PBOC Announces New Capital Requirements for Digital Banks", "Date": "March 8, 2025", 
     "Image": "https://images.unsplash.com/photo-1598257006458-087169a1f08d?w=800&h=600&fit=crop&auto=format", 
     "Description": "The People's Bank of China has established new capital requirements specifically tailored for digital banking institutions."},
    
    {"Region": "Singapore", "Update": "MAS Revises Digital Asset Licensing Framework", "Date": "March 5, 2025", 
     "Image": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Monetary Authority of Singapore has revised its licensing framework for digital asset service providers."},
    
    {"Region": "UAE", "Update": "DFSA Implements New FinTech Regulations", "Date": "March 3, 2025", 
     "Image": "https://images.unsplash.com/photo-1546412414-e1885e51cfa5?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Dubai Financial Services Authority has implemented new regulations to support the growth of FinTech innovation."},
    
    {"Region": "Brazil", "Update": "CVM Updates Securities Regulations", "Date": "March 1, 2025", 
     "Image": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Brazilian Securities Commission has updated regulations to enhance market transparency and investor protection."},
    
    {"Region": "Germany", "Update": "BaFin Introduces Stricter AML Guidelines", "Date": "February 28, 2025", 
     "Image": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Federal Financial Supervisory Authority has introduced stricter anti-money laundering guidelines for financial institutions."},
    
    {"Region": "Japan", "Update": "FSA Strengthens Digital Asset Regulations", "Date": "February 25, 2025", 
     "Image": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=800&h=600&fit=crop&auto=format", 
     "Description": "The Financial Services Agency has strengthened regulations governing digital assets and cryptocurrency exchanges."}
]

# Sidebar for navigation
st.sidebar.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=200&h=200&fit=crop&auto=format", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Latest Updates", "Compliance Report","Login"])

if page == "Home":
    st.markdown("<div class='subheader'>Stay ahead with the latest financial regulations</div>", unsafe_allow_html=True)

    # Key Features Section
    st.header("Key Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📰</div>
            <h3>Real-Time Regulatory Updates</h3>
            <p>Track regulatory changes globally in real-time.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI-Driven Risk Analysis</h3>
            <p>Identify compliance gaps and fraud risks with predictive analytics.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚙️</div>
            <h3>Automated Audits</h3>
            <p>Ensure processes meet regulatory standards effortlessly.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🕵️</div>
            <h3>Fraud Detection & AML</h3>
            <p>Detect and prevent fraudulent activities with advanced ML algorithms.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📋</div>
            <h3>KYC Tools</h3>
            <p>Automate customer background checks for identity verification.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <h3>Cybersecurity Protection</h3>
            <p>Safeguard sensitive data from malware and cyber threats.</p>
            <button class="custom-button">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

    # Global Reach Section
    st.header("Global Reach")
    st.subheader("Compliance Without Borders")
    st.write(
        "Our platform supports regulatory requirements across 100+ jurisdictions, ensuring you stay compliant no matter where you operate.")

    # Define map data for PyDeck with more accurate coordinates and information
    map_data = pd.DataFrame([
        {"lat": 38.9, "lon": -77.0, "name": "USA", "size": 100, "color": [76, 28, 97]},
        {"lat": 50.8, "lon": 4.4, "name": "EU", "size": 100, "color": [0, 51, 153]},
        {"lat": 51.5, "lon": -0.1, "name": "UK", "size": 100, "color": [204, 0, 0]},
        {"lat": 39.9, "lon": 116.4, "name": "China", "size": 100, "color": [204, 0, 0]},
        {"lat": 1.3, "lon": 103.8, "name": "Singapore", "size": 100, "color": [204, 0, 0]},
        {"lat": 25.2, "lon": 55.3, "name": "UAE", "size": 100, "color": [0, 102, 0]},
        {"lat": -15.8, "lon": -47.9, "name": "Brazil", "size": 100, "color": [0, 153, 0]},
        {"lat": 52.5, "lon": 13.4, "name": "Germany", "size": 100, "color": [0, 0, 0]},
        {"lat": 35.7, "lon": 139.8, "name": "Japan", "size": 100, "color": [204, 0, 0]}
    ])

    # Create the map
    view_state = pdk.ViewState(
        latitude=20,
        longitude=0,
        zoom=1.5,
        pitch=40,
        bearing=0
    )

    # Create the scatter plot layer with custom colors
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position=["lon", "lat"],
        get_radius="size",
        get_fill_color="color",
        pickable=True,
        auto_highlight=True,
        opacity=0.8
    )

    # Create the tooltip
    tooltip = {
        "html": "<b>{name}</b>",
        "style": {"background": "rgba(74, 28, 97, 0.8)", "color": "white", "font-family": "sans-serif",
                  "padding": "10px"}
    }

    # Render the map
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer],
        tooltip=tooltip
    ))

    # Display regulatory info when a region is selected
    selected_region = st.selectbox("Select region for detailed regulations",
                                   options=[update["Region"] for update in updates])

    # Show the selected region's update
    for update in updates:
        if update["Region"] == selected_region:
            st.markdown(f"<div class='update-container'>", unsafe_allow_html=True)
            st.markdown(f"### {update['Region']} Regulations")
            st.image(update['Image'], width=400)
            st.write(f"**Latest Update:** {update['Update']}")
            st.write(f"**Date:** {update['Date']}")
            st.write(update['Description'])
            st.markdown("</div>", unsafe_allow_html=True)
            break

    # Pricing or Subscription Plans
    st.header("Pricing Plans")
    st.markdown("""
    <table class="pricing-table">
        <tr>
            <th>Plan</th>
            <th>Features</th>
            <th>Action</th>
        </tr>
        <tr>
            <td><strong>Basic</strong></td>
            <td>Real-time regulatory updates, basic risk analysis</td>
            <td><button class="custom-button">Sign Up</button></td>
        </tr>
        <tr>
            <td><strong>Pro</strong></td>
            <td>Advanced fraud detection, AML tools, automated audits</td>
            <td><button class="custom-button">Sign Up</button></td>
        </tr>
        <tr>
            <td><strong>Enterprise</strong></td>
            <td>Custom compliance reports, consulting services, priority support</td>
            <td><button class="custom-button">Contact Us</button></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # Footer with Key Links
    st.markdown("""
    <div class="footer">
        <p><strong>Global Compliance Hub:</strong> Your One-Stop Solution for Real-Time Regulatory Compliance.</p>
        <p>
            <a href="#features">Features</a> | 
            <a href="#pricing">Pricing</a> | 
            <a href="#about">About Us</a> | 
            <a href="#contact">Contact Us</a> | 
            <a href="#blog">Blog/Resources</a>
        </p>
        <p>
            <a href="https://linkedin.com">LinkedIn</a> | 
            <a href="https://twitter.com">Twitter</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Latest Updates":
    st.write("### Latest Regulation Updates")

    # Expanded database of regulatory updates with links to official documents
    updates = [
        {
            "Region": "USA",
            "Update": "SEC Finalizes New Climate Disclosure Rules",
            "Date": "March 15, 2025",
            "Image": "https://images.unsplash.com/photo-1621944190310-e3cca1564bd7?w=800&h=600&fit=crop&auto=format",
            "Description": "The Securities and Exchange Commission has finalized rules requiring public companies to disclose climate-related financial risks.",
            "Document": "https://www.sec.gov/news/press-release/2025-123",
            "Sector": "Climate, Corporate Governance"
        },
        {
            "Region": "EU",
            "Update": "ECB Updates Digital Euro Framework",
            "Date": "March 12, 2025",
            "Image": "https://images.unsplash.com/photo-1580674285054-bed31e145f59?w=800&h=600&fit=crop&auto=format",
            "Description": "The European Central Bank has released a comprehensive framework for the implementation of the Digital Euro.",
            "Document": "https://www.ecb.europa.eu/press/pr/date/2025/html/pr250312.en.html",
            "Sector": "Digital Currency, Banking"
        },
        {
            "Region": "UK",
            "Update": "FCA Introduces Enhanced Consumer Protection Rules",
            "Date": "March 10, 2025",
            "Image": "https://images.unsplash.com/photo-1486299267070-83823f5448dd?w=800&h=600&fit=crop&auto=format",
            "Description": "The Financial Conduct Authority has implemented new rules to strengthen consumer protection in financial services.",
            "Document": "https://www.fca.org.uk/news/press-releases/fca-introduces-enhanced-consumer-protection-rules",
            "Sector": "Consumer Protection, Financial Services"
        },
        {
            "Region": "China",
            "Update": "PBOC Announces New Capital Requirements for Digital Banks",
            "Date": "March 8, 2025",
            "Image": "https://images.unsplash.com/photo-1598257006458-087169a1f08d?w=800&h=600&fit=crop&auto=format",
            "Description": "The People's Bank of China has established new capital requirements specifically tailored for digital banking institutions.",
            "Document": "https://www.pbc.gov.cn/en/3688110/3688172/4563176/index.html",
            "Sector": "Digital Banking, Capital Requirements"
        },
        {
            "Region": "Singapore",
            "Update": "MAS Revises Digital Asset Licensing Framework",
            "Date": "March 5, 2025",
            "Image": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800&h=600&fit=crop&auto=format",
            "Description": "The Monetary Authority of Singapore has revised its licensing framework for digital asset service providers.",
            "Document": "https://www.mas.gov.sg/news/media-releases/2025/mas-revises-digital-asset-licensing-framework",
            "Sector": "Digital Assets, Licensing"
        },
        {
            "Region": "UAE",
            "Update": "DFSA Implements New FinTech Regulations",
            "Date": "March 3, 2025",
            "Image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&h=600&fit=crop&auto=format",
            "Description": "The Dubai Financial Services Authority has implemented new regulations to support the growth of FinTech innovation.",
            "Document": "https://www.dfsa.ae/FinTech-Regulations-2025",
            "Sector": "FinTech, Innovation"
        },
        {
            "Region": "Brazil",
            "Update": "CVM Updates Securities Regulations",
            "Date": "March 1, 2025",
            "Image": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800&h=600&fit=crop&auto=format",
            "Description": "The Brazilian Securities Commission has updated regulations to enhance market transparency and investor protection.",
            "Document": "https://www.cvm.gov.br/noticias/cvm-updates-securities-regulations-2025",
            "Sector": "Securities, Investor Protection"
        },
        {
            "Region": "Germany",
            "Update": "BaFin Introduces Stricter AML Guidelines",
            "Date": "February 28, 2025",
            "Image": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800&h=600&fit=crop&auto=format",
            "Description": "The Federal Financial Supervisory Authority has introduced stricter anti-money laundering guidelines for financial institutions.",
            "Document": "https://www.bafin.de/EN/Aufsicht/AML/aml_node_en.html",
            "Sector": "AML, Financial Regulation"
        },
        {
            "Region": "Japan",
            "Update": "FSA Strengthens Digital Asset Regulations",
            "Date": "February 25, 2025",
            "Image": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=800&h=600&fit=crop&auto=format",
            "Description": "The Financial Services Agency has strengthened regulations governing digital assets and cryptocurrency exchanges.",
            "Document": "https://www.fsa.go.jp/en/news/2025/20250225.html",
            "Sector": "Digital Assets, Cryptocurrency"
        },
        {
            "Region": "Australia",
            "Update": "ASIC Introduces New ESG Reporting Requirements",
            "Date": "February 20, 2025",
            "Image": "https://images.unsplash.com/photo-1501167786227-4cba60f6d58f?w=800&h=600&fit=crop&auto=format",
            "Description": "The Australian Securities and Investments Commission has introduced new ESG reporting requirements for listed companies.",
            "Document": "https://asic.gov.au/regulatory-resources/find-a-document/guidance/2025-esg-reporting-requirements/",
            "Sector": "ESG, Corporate Reporting"
        },
        {
            "Region": "Canada",
            "Update": "OSFI Updates Cybersecurity Guidelines",
            "Date": "February 18, 2025",
            "Image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&h=600&fit=crop&auto=format",
            "Description": "The Office of the Superintendent of Financial Institutions has updated its cybersecurity guidelines for financial institutions.",
            "Document": "https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/cyber-resilience/Pages/default.aspx",
            "Sector": "Cybersecurity, Financial Regulation"
        },
        {
            "Region": "India",
            "Update": "SEBI Enhances Corporate Governance Norms",
            "Date": "February 15, 2025",
            "Image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&h=600&fit=crop&auto=format",
            "Description": "The Securities and Exchange Board of India has enhanced corporate governance norms for listed companies.",
            "Document": "https://www.sebi.gov.in/legal/circulars/feb-2025/corporate-governance-norms_50000.html",
            "Sector": "Corporate Governance, Securities"
        }
    ]

    # Convert updates to DataFrame
    data = pd.DataFrame(updates)

    # Display updates with images and links
    st.write("### Browse All Updates")
    for update in updates:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(update['Image'], use_container_width=True)
        with col2:
            st.markdown(f"<div class='update-container'>", unsafe_allow_html=True)
            st.markdown(f"<div class='update-header'>{update['Region']}: {update['Update']}</div>",
                        unsafe_allow_html=True)
            st.markdown(f"<div class='update-date'>📅 {update['Date']}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='update-tags'>🏷️ <b>Region:</b> {update['Region']} | <b>Sector:</b> {update['Sector']}</div>",
                unsafe_allow_html=True)
            st.write(update['Description'])
            st.markdown(f"[Read the official document]({update['Document']})", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")

    # Add filter options
    st.write("### Filter Updates")
    selected_region = st.multiselect("Filter by Region", options=list(set([u["Region"] for u in updates])))
    selected_sector = st.multiselect("Filter by Sector", options=list(set([u["Sector"] for u in updates])))

    if selected_region or selected_sector:
        filtered_data = data[
            (data["Region"].isin(selected_region) if selected_region else True) &
            (data["Sector"].isin(selected_sector) if selected_sector else True)
            ]
        st.write(f"### Filtered Results ({len(filtered_data)} updates)")
        for _, row in filtered_data.iterrows():
            col1, col2 = st.columns([2, 3])
            with col1:
                st.image(row['Image'], use_container_width=True)
            with col2:
                st.markdown(f"<div class='update-container'>", unsafe_allow_html=True)
                st.markdown(f"<div class='update-header'>{row['Region']}: {row['Update']}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"<div class='update-date'>📅 {row['Date']}</div>", unsafe_allow_html=True)
                st.markdown(
                    f"<div class='update-tags'>🏷️ <b>Region:</b> {row['Region']} | <b>Sector:</b> {row['Sector']}</div>",
                    unsafe_allow_html=True)
                st.write(row['Description'])
                st.markdown(f"[Read the official document]({row['Document']})", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")

elif page == "Compliance Report":
    st.write("### Generate Regulation Compliance Report")

    # Input fields for company details
    company_name = st.text_input("Company Name")
    industry = st.selectbox("Industry", [
        "Banking", "Insurance", "FinTech", "Cryptocurrency", "Investment",
        "Manufacturing", "Healthcare", "Technology", "Energy", "Retail",
        "Telecommunications", "Transportation", "Pharmaceuticals", "Agriculture", "Other"
    ])
    operations = st.multiselect("Operations", [
        # Financial Operations
        "Retail Banking", "Corporate Banking", "Asset Management", "Trading",
        "Payment Processing", "Lending", "Insurance Underwriting", "Cryptocurrency Exchange",

        # Non-Financial Operations
        "Product Manufacturing", "Supply Chain Management", "Pharmaceutical Production",
        "Medical Device Manufacturing", "Software Development", "Cloud Services",
        "Data Centers", "Renewable Energy Production", "Oil and Gas Extraction",
        "Retail Sales", "E-commerce", "Telecom Services", "Network Infrastructure",
        "Aviation", "Maritime Transport", "Rail Transport", "Road Transport",
        "Crop Production", "Livestock Farming", "Food Processing"
    ])

    # Button to generate the report
    if st.button("Generate Compliance Report"):
        st.write(f"### Compliance Report for {company_name}")
        st.write(f"**Industry:** {industry}")
        st.write(f"**Operations:** {', '.join(operations)}")

        # Expanded compliance data based on industry and operations
        compliance_data = {
            # Financial Industries
            "Banking": {
                "Retail Banking": [
                    {"regulation": "Basel III Compliance",
                     "details": "Maintain minimum capital requirements, leverage ratios, and liquidity coverage ratios. Regularly report to regulatory authorities.",
                     "link": "https://www.bis.org/bcbs/basel3.htm"},
                    {"regulation": "Anti-Money Laundering (AML) Regulations",
                     "details": "Implement customer due diligence (CDD) procedures, monitor transactions for suspicious activity, and file suspicious activity reports (SARs).",
                     "link": "https://www.fincen.gov/resources/statutes-and-regulations"},
                ],
                "Corporate Banking": [
                    {"regulation": "Basel III Compliance",
                     "details": "Maintain higher capital buffers for systemic importance, conduct stress testing, and report to regulators.",
                     "link": "https://www.bis.org/bcbs/basel3.htm"},
                    {"regulation": "Large Exposure Framework",
                     "details": "Limit exposure to a single counterparty to avoid concentration risk.",
                     "link": "https://www.bis.org/bcbs/publ/d445.htm"},
                ],
            },
            "Insurance": {
                "Insurance Underwriting": [
                    {"regulation": "Solvency II",
                     "details": "Maintain adequate capital reserves, conduct regular risk assessments, and submit quarterly and annual reports to regulators.",
                     "link": "https://www.eiopa.europa.eu/browse/regulation-and-policy/solvency-ii_en"},
                    {"regulation": "IFRS 17",
                     "details": "Adopt new accounting standards for insurance contracts, ensure accurate measurement of liabilities, and disclose relevant information in financial statements.",
                     "link": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/"},
                ],
            },
            # Non-Financial Industries
            "Manufacturing": {
                "Product Manufacturing": [
                    {"regulation": "ISO 9001 Quality Management",
                     "details": "Implement a quality management system (QMS), conduct regular audits, and continuously improve processes.",
                     "link": "https://www.iso.org/iso-9001-quality-management.html"},
                    {"regulation": "Environmental Regulations",
                     "details": "Monitor and reduce emissions, manage waste disposal responsibly, and comply with local environmental laws.",
                     "link": "https://www.epa.gov/laws-regulations"},
                ],
            },
            "Healthcare": {
                "Pharmaceutical Production": [
                    {"regulation": "FDA Regulations",
                     "details": "Follow Good Manufacturing Practices (GMP), ensure product safety and efficacy, and maintain detailed records for inspections.",
                     "link": "https://www.fda.gov/regulatory-information"},
                    {"regulation": "Good Manufacturing Practices (GMP)",
                     "details": "Establish quality control systems, train staff, and validate manufacturing processes.",
                     "link": "https://www.fda.gov/drugs/pharmaceutical-quality-resources/good-manufacturing-practices-gmp-guidance-information"},
                ],
            },
            "Technology": {
                "Software Development": [
                    {"regulation": "GDPR",
                     "details": "Obtain explicit consent for data collection, implement data protection measures, and appoint a Data Protection Officer (DPO).",
                     "link": "https://gdpr-info.eu/"},
                    {"regulation": "Cybersecurity Regulations",
                     "details": "Conduct regular vulnerability assessments, encrypt sensitive data, and establish incident response plans.",
                     "link": "https://www.nist.gov/cyberframework"},
                ],
            },
            "Energy": {
                "Renewable Energy Production": [
                    {"regulation": "Renewable Energy Standards",
                     "details": "Comply with renewable portfolio standards (RPS) and ensure grid compatibility.",
                     "link": "https://www.epa.gov/statelocalenergy/state-renewable-energy-resources"},
                    {"regulation": "Environmental Impact Regulations",
                     "details": "Conduct environmental impact assessments (EIAs) and mitigate negative impacts.",
                     "link": "https://www.epa.gov/nepa"},
                ],
            },
            "Retail": {
                "Retail Sales": [
                    {"regulation": "Consumer Protection Laws",
                     "details": "Ensure transparent pricing, accurate product labeling, and fair return policies.",
                     "link": "https://www.ftc.gov/tips-advice/business-center/guidance/consumer-protection-laws"},
                    {"regulation": "Product Safety Standards",
                     "details": "Test products for safety, comply with labeling requirements, and report defects.",
                     "link": "https://www.cpsc.gov/Regulations-Laws--Standards"},
                ],
            },
            "Telecommunications": {
                "Telecom Services": [
                    {"regulation": "Telecom Regulatory Authority (TRA) Compliance",
                     "details": "Obtain necessary licenses, comply with spectrum allocation rules, and ensure service quality.",
                     "link": "https://www.tra.gov.ae/"},
                    {"regulation": "Data Privacy Laws",
                     "details": "Protect customer data, obtain consent for data usage, and comply with local privacy laws.",
                     "link": "https://gdpr-info.eu/"},
                ],
            },
            "Transportation": {
                "Aviation": [
                    {"regulation": "Federal Aviation Regulations (FAR)",
                     "details": "Comply with safety standards, maintain aircraft, and train staff.",
                     "link": "https://www.faa.gov/regulations_policies/faa_regulations/"},
                    {"regulation": "International Civil Aviation Organization (ICAO) Standards",
                     "details": "Adhere to international aviation safety and security standards.",
                     "link": "https://www.icao.int/"},
                ],
            },
            "Agriculture": {
                "Crop Production": [
                    {"regulation": "Good Agricultural Practices (GAP)",
                     "details": "Follow sustainable farming practices, ensure food safety, and maintain traceability.",
                     "link": "https://www.fao.org/gap/home/en/"},
                    {"regulation": "Pesticide Regulations",
                     "details": "Use approved pesticides, follow application guidelines, and maintain records.",
                     "link": "https://www.epa.gov/pesticide-registration"},
                ],
            },
            # Add more industries and operations as needed...
        }

        # Generate the compliance report
        st.write("### Applicable Regulations")
        for operation in operations:
            if operation in compliance_data.get(industry, {}):
                st.write(f"**{operation}:**")
                for regulation in compliance_data[industry][operation]:
                    st.write(f"- **{regulation['regulation']}**")
                    st.write(f"  **How to Comply:** {regulation['details']}")
                    st.write(f"  **Learn More:** [Official Link]({regulation['link']})")
            else:
                st.write(f"**{operation}:** No specific regulations found.")

        st.write("### General Recommendations")
        st.write(
            "1. **Conduct Regular Audits:** Perform internal and external audits to ensure compliance with all applicable regulations.")
        st.write(
            "2. **Train Employees:** Provide regular training to employees on compliance requirements and best practices.")
        st.write(
            "3. **Maintain Documentation:** Keep detailed records of compliance efforts, including policies, procedures, and audit reports.")
        st.write("4. **Stay Updated:** Monitor regulatory changes and update your compliance programs accordingly.")
        st.write(
            "5. **Consult Experts:** Work with legal and compliance experts to address complex regulatory requirements.")

        st.write("### Disclaimer")
        st.write(
            "This report is generated based on general industry standards and may not cover all specific regulatory requirements for your company. Consult with a legal expert for detailed compliance advice.")

elif page == "Login":
    st.write("### User Login")
    
    # Use more secure approach for authentication
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Store valid users in a separate dictionary (in a real app, use a database)
    valid_users = {
        "admin": "secure_password_123",
        "user": "user_password_456"
    }
    
    if st.button("Login"):
        if username in valid_users and password == valid_users[username]:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.write("Welcome to the Financial Regulations Hub admin panel!")
        else:
            st.error("Invalid credentials. Please try again.")
            st.session_state.logged_in = False
    
    # Show additional info only if logged in
    if st.session_state.get('logged_in', False):
        st.write("### Admin Panel")
        st.write("Here you can manage regulatory updates and system settings.")
        
        # Add tabs for different admin functions
        admin_tab1, admin_tab2, admin_tab3 = st.tabs(["Add Update", "Edit Updates", "System Settings"])
        
        with admin_tab1:
            st.write("### Add New Regulatory Update")
            new_region = st.selectbox("Region", options=["USA", "EU", "UK", "China", "Singapore", "UAE", "Brazil", "Germany", "Japan", "Other"])
            new_update = st.text_input("Update Title")
            new_description = st.text_area("Description")
            new_date = st.date_input("Date")
            
            if st.button("Add Update"):
                st.success("Update added successfully! (Simulated)")
        
        with admin_tab2:
            st.write("### Edit Existing Updates")
            edit_update = st.selectbox("Select Update to Edit", options=[f"{u['Region']}: {u['Update']}" for u in updates])
            
            if edit_update:
                st.text_area("Edit Description", value=next((u["Description"] for u in updates if f"{u['Region']}: {u['Update']}" == edit_update), ""))
                if st.button("Save Changes"):
                    st.success("Changes saved successfully! (Simulated)")
        
        with admin_tab3:
            st.write("### System Settings")
            st.checkbox("Enable email notifications")
            st.checkbox("Enable API access")
            st.slider("Data retention period (days)", 30, 365, 180)
            
            if st.button("Save Settings"):
                st.success("Settings saved successfully! (Simulated)")

# Footer
st.write("""
    ---
    *© 2025 Global Financial Regulations Hub. All rights reserved.*
""")
