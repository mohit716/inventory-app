# Inventory App (FastAPI + React + MongoDB)

Small full-stack demo: React (Vite) frontend talking to a FastAPI backend with MongoDB.  
Validation with Pydantic v2, dependency injection/service layer, API-key secured write endpoints, Swagger docs, pagination/search, and basic optimization.

## Stack
- **Frontend:** React (Vite)
- **Backend:** FastAPI, Pydantic v2
- **Database:** MongoDB (local or Atlas)
- **Auth:** API key via `X-Api-Key` (Swagger **Authorize**)
- **Architecture:** Modular (routes, services, models, db, security)

## Quickstart

### 1. Environment
Create a `.env` in `inventory-backend/` with:
```env
MONGO_URI=mongodb://localhost:27017
API_KEY=your-api-key
```

### 2. Run backend
```bash
cd inventory-backend
# activate your venv if not already
uvicorn main:app --reload
```
Swagger UI: http://127.0.0.1:8000/docs — click **Authorize** and enter your API key (header name `X-Api-Key`).

### 3. Run frontend
```bash
cd inventory-frontend
npm install    # if you haven't already
npm run dev
```
Open: http://localhost:5173

## API

### GET /items
List items. Supports pagination and search.
Query parameters:
- `skip` (int, default 0)
- `limit` (int, default 50)
- `q` (optional filter substring on name or category)

Example:
```
GET /items?skip=0&limit=5&q=app
```

### POST /items
Add a new item (requires API key).
Body example:
```json
{
  "name": "apple",
  "category": "fruit",
  "quantity": 10
}
```

## Features & Optimizations
- **Input validation** using Pydantic v2 (`Annotated` + `Field`), strict models.
- **Dependency injection / service layer** (`ItemService`) for separation of concerns.
- **Security:** API-key auth enforced on POST with Swagger Authorize support.
- **Pagination & search:** `skip`, `limit`, and `q` filter on `/items`.
- **Projection:** `_id` removed from responses to match schema.
- **Index:** Created `name` index in Mongo for faster filtering:
  ```js
  db.items.createIndex({ name: 1 })
  ```

## Cross-browser
Tested on:
- Chrome (Chromium)
- Edge (Chromium)
- *(optional)* Firefox

Screenshot evidence: `docs/screens/`  
![Chrome Screenshot](docs/screens/ui-chrome.png)  
![Edge Screenshot](docs/screens/ui-edge.png)

## Jira & Workflow
Jira board screenshot: `docs/jira/board.png`  
Work tracked via branch-per-feature and PRs. Example PRs:
- Service layer / DI implementation  
- Bug reproduction & fix (ObjectId projection)  
- Pagination + search enhancement  
- Documentation updates (README, screenshots, Jira)

## Project Structure
```
inventory-backend/
  routes/
    items.py
  services/
    items_service.py
  models.py
  db.py
  security.py
inventory-frontend/
docs/
  screens/
  jira/
README.md
```

## Demo Checklist (what to show in interview)
1. Start backend and show `/docs`.  
2. Authorize with API key, `POST /items`, then `GET /items?skip=0&limit=2&q=...`.  
3. Start frontend, add an item, observe it appears.  
4. Show pagination working.  
5. Show Jira board screenshot.  
6. Show PR history (service layer, bug fix, pagination, docs).  
7. Explain architecture: routers → service → DB, and security/validation.

## Contact / Notes
- GitHub: https://github.com/mohit716/inventory-app  
- Use this as a reference implementation; can be extended to product/catalog use cases.
