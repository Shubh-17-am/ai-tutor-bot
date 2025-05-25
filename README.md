# AI Tutor Bot (Vercel Deployment)

## Overview
AI Tutor Bot built using FastAPI, deployed to Vercel, powered by Gemini API. It includes:
- Tutor Agent
- Math and Physics Sub-Agents
- Calculator and Constants Tool

## Local Setup
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```

## Deployment (Vercel)
1. Push code to GitHub
2. Import repo in Vercel
3. Set environment variable: `GEMINI_API_KEY`
4. Vercel will auto-deploy using `vercel.json`

## Test
POST `/ask/` with JSON: `{ "query": "What is Newton's second law?" }`