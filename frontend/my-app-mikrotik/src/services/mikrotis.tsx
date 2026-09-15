import {apiFetch} from './api';


export async function getMikrotikData() {
    try {
        const data = await apiFetch('/mikrotik');
        console.log('Mikrotik data fetched:', data);
        return data;
    } catch (error) {
        console.error('Error fetching Mikrotik data:', error);
        throw error;
    }
}