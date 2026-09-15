const API_URL = "http://127.0.0.1:8000";

export async function apiFetch(
    endpoint: string,
    options: RequestInit = {}
) {
    const url = `${API_URL}${endpoint}`;

    console.log("Haciendo petición:", url);

    try {
        const response = await fetch(url, {
            headers: {
                "Content-Type": "application/json",
                ...options.headers,
            },
            ...options,
        });

        console.log("Status HTTP:", response.status);

        if (!response.ok) {
            throw new Error(
                `Error HTTP: ${response.status} ${response.statusText}`
            );
        }

        const data = await response.json();

        console.log("Respuesta API:", data);

        return data;

    } catch (error) {
        console.error("ERROR EN apiFetch:", error);
        throw error;
    }
}