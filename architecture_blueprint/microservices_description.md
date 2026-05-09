# Microservices Architecture

*   **API Gateway**: Acts as the central entry point for all client requests, managing routing to specific backend services and handling authentication tokens.
*   **Authentication Service**: Dedicated service for managing user identity, registration, and secure JWT-based login sessions with its own database.
*   **Itinerary Planning Service**: An AI-powered microservice responsible for processing travel preferences and generating customized trip schedules.
*   **Payment Service**: Handles all financial interactions, including credit card processing and billing history, isolated from other business logic.
*   **Collaboration Service**: Manages real-time data synchronization between multiple users during group trip planning sessions.
*   **Notification Service**: A standalone service that triggers and sends push notifications, emails, and SMS alerts based on system events.
*   **User Profile Service**: Maintains detailed user metadata, travel preferences, and account settings in a dedicated user database.
*   **Inventory Service**: Manages real-time availability data for flights and hotels by communicating with external travel partner APIs.
