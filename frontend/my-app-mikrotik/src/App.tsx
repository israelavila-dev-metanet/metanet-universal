import { useState, useEffect } from 'react';
import {getMikrotikData} from './services/mikrotis.tsx';
import './App.css'

function App() {
const [mikrotik, setMikrotik] = useState<any[]>([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState<string | null>(null);

useEffect(() => {
  const fetchData = async () => {
    console.log('Mikrotik data in App component:');
    try {
      const data = await getMikrotikData();
      setMikrotik(data);
      setLoading(false);
    }catch (error) {
    console.error('ERROR EN APP:', error);
    setError(String(error));
    setLoading(false);
    }
    // } catch (error) {
    //   setError('Error fetching data');
    //   setLoading(false);
    // }
  };

  fetchData();
}, []);

if (loading) {
  return <div>Loading...</div>;
}

if (error) {
  return <div>{error}</div>;
} 

  return (
    <>

    <div className="min-h-screen flex flex-col bg-gray-100">
    <header className="flex bg-gray-800 text-white text-center">
          <nav className="flex items-center space-x-4 text-center"> 
                <ul className="flex justify-between space-x-4 gap-4 text-center">
                  <li><p className="text-center">Mikrotik API</p></li>
                  <li><p className="text-center">Devices</p></li>
                </ul>
          </nav>
    </header>
    <main className="flex-1 p-6">
      <table className="border-separate border border-gray-400 ...">
        <thead>
          <tr>
            <th className="border border-gray-300 ...">dsdsf</th>
            <th className="border border-gray-300 ...">sdf</th>
            <th className="border border-gray-300 ...">IDENTITY</th>
            <th className="border border-gray-300 ...">VERSION</th>
            <th className="border border-gray-300 ...">PPOE-USERS</th>
            <th className="border border-gray-300 ...">PPOE-USERasdS</th>
            <th className="border border-gray-300 ...">ACCIONES</th>
          </tr>
        </thead>

          <tbody>
        {Object.entries(mikrotik).map(([id, router]: [string, any]) => (
          <tr key={id}>

            <td className="border border-gray-300 px-4 py-2">
              {router.identity}
            </td>

            <td className="border border-gray-300 px-4 py-2">
              {router.version}
            </td>

            <td className="border border-gray-300 px-4 py-2 text-center">
              {router.pppoe_users}
            </td>

            <td className="border border-gray-300 px-4 py-2">
              {router.host}
            </td>

            <td className="border border-gray-300 px-4 py-2">
              <button
                className="bg-blue-500 text-white px-3 py-1 rounded"
                onClick={() => console.log("Router seleccionado:", id, router)}
              >
                Ver
              </button>
            </td>

          </tr>
        ))}
      </tbody>
   
      </table>
    </main>

    <footer className="bg-gray-800 text-white p-4 text-center text-sm">
        &copy; 2026 IJAM&SOFIA. All rights reserved.
    </footer>
    </div>
   
   
    </>
  )
}

export default App
