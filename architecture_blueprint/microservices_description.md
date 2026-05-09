# Microservices Architecture

*   **API Gateway**: The central entry point that handles all incoming requests, routing them to the correct microservice and managing global rate limiting.
*   **Auth Service**: Manages user authentication and authorization using JWT tokens, operating with a dedicated identity database.
*   **Itinerary Service**: Core AI engine that processes trip requests and generates travel plans, storing results in its own itinerary database.
*   **Payment Service**: An isolated service that processes payments and manages transaction logs, ensuring high security for financial data.
*   **Group Collaboration Service**: Enables real-time, multi-user editing of travel plans using WebSockets to synchronize changes across group members.
*   **Notification Service**: Handles the asynchronous delivery of push notifications, SMS, and emails triggered by trip updates or booking status.
*   **User Profile Service**: Manages sensitive user metadata, travel preferences, and account settings in a strictly isolated user database.
*   **Inventory Service**: Communicates with external travel provider APIs (GDS) to fetch and cache real-time availability for flights and hotels.
