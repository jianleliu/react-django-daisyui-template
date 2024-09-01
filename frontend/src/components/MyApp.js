// src/components/MyApp.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MyApp() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/api/myapp')
      .then(response => {
        setData(response.data);
        console.log(response.data)
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error fetching data: {error.message}</p>;

  return (
    <div>
      <h1>My App</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>
            <h2>{item.item}</h2>
            <p>{item.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MyApp;
