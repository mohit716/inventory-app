import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({ name: "", category: "", quantity: 0 });
  const [q, setQ] = useState("");

  const load = async () => {
    const res = await axios.get(`${API}/items`);
    setItems(res.data);
  };

  useEffect(() => { load(); }, []);

  const onChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const addItem = async () => {
    await axios.post(`${API}/items`, form, {
      headers: { "x-api-key": "secret123" }
    });
    setForm({ name: "", category: "", quantity: 0 });
    load();
  };

  const filtered = items.filter(
    (it) =>
      it.name.toLowerCase().includes(q.toLowerCase()) ||
      (it.category || "").toLowerCase().includes(q.toLowerCase())
  );

  return (
    <div className="container py-4">
      <h2 className="mb-3">Inventory</h2>

      <input
        className="form-control mb-3"
        placeholder="Search by name or category"
        value={q}
        onChange={(e) => setQ(e.target.value)}
      />

      <ul className="list-group mb-4">
        {filtered.map((it, i) => (
          <li key={i} className="list-group-item d-flex justify-content-between">
            <span>{it.name} <small className="text-muted">({it.category})</small></span>
            <span>Qty: {it.quantity}</span>
          </li>
        ))}
      </ul>

      <h4 className="mb-2">Add Item</h4>
      <div className="row g-2">
        <div className="col-md-4">
          <input name="name" className="form-control" placeholder="Name"
                 value={form.name} onChange={onChange}/>
        </div>
        <div className="col-md-4">
          <input name="category" className="form-control" placeholder="Category"
                 value={form.category} onChange={onChange}/>
        </div>
        <div className="col-md-2">
          <input name="quantity" type="number" className="form-control" placeholder="Qty"
                 value={form.quantity} onChange={onChange}/>
        </div>
        <div className="col-md-2 d-grid">
          <button className="btn btn-primary" onClick={addItem}>Add</button>
        </div>
      </div>
    </div>
  );
}
