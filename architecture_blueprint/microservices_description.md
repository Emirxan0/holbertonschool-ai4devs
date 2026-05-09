# Microservices Architecture

*   **API Gateway**: The single entry point for all client requests, routing them to the appropriate microservices and handling load balancing.
*   **Auth Service**: Manages user identity, authentication, and authorization independently with its own secure database.
*   **Itinerary Service**: Handles the core AI logic for generating and managing travel plans and trip suggestions.
*   **Payment Service**: Processes financial transactions and integrates with external payment providers.
*   **Collaboration Service**: Manages real-time data synchronization for group planning and multi-user editing.
*   **Notification Service**: An isolated service responsible for sending push notifications, SMS, and emails based on system events.
*   **User Service**: Manages detailed user profiles, preferences, and account settings.
*   **Database per Service**: Each microservice (Auth, Itinerary, Payment, etc.) has its own dedicated database to ensure complete isolation and scalability.
