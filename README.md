🚨 AI-Based Suspicious Email Detection and Automated Response System
Overview

An AI-powered email security system that detects phishing, scam, and suspicious emails, assigns a risk score, explains the reasons behind the score, and automates email responses using n8n workflows.

Features
📧 Email ingestion from Gmail/Outlook
🤖 AI-powered email content analysis using LLMs
⚠️ Risk scoring system (0–100)
🔍 Detection of phishing, spoofing, malicious links, and social engineering attempts
📝 Explainable AI risk reports
🔄 Automated email replies using n8n
🚨 Security alerts for high-risk emails
📊 Dashboard for monitoring email threats
Risk Classification
Score Range	Risk Level
0–20	Safe
21–40	Low Risk
41–60	Medium Risk
61–80	High Risk
81–100	Critical
System Architecture
Email Inbox
    ↓
n8n Trigger
    ↓
Email Extraction
    ↓
LLM Analysis
    ↓
Risk Scoring Engine
    ↓
Classification
    ↓
Database
    ↓
Dashboard & Alerts
    ↓
Automated Response
Tech Stack
Backend
Python
FastAPI
AI & Automation
Groq API
LangChain
n8n
Database
PostgreSQL
Frontend
Next.js
Tailwind CSS
Integrations
Gmail API
Outlook API
How It Works
New email arrives in the inbox.
n8n automatically triggers the workflow.
Email content is sent to the AI analysis service.
The LLM evaluates potential threats.
A risk score is generated.
High-risk emails trigger alerts.
Safe emails receive automated responses.
Results are stored and displayed on the dashboard.
Future Enhancements
VirusTotal integration
Google Safe Browsing checks
Attachment malware analysis
Multi-language support
Multi-agent threat analysis
Real-time threat intelligence feeds
Project Goals

This project aims to combine:

Generative AI
Workflow Automation
Cybersecurity
Explainable AI
Full-Stack Development

to create a practical email security assistant for individuals and organizations.

Developed by: Shubhod Loni, Suraj M N
GitHub: ShubhodLoni
        Suraj-M-N
