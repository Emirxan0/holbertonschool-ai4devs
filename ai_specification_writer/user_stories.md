# User Stories

### User Story 1
As a passenger, I want to search for nearby drivers so that I can find a quick ride.
**Acceptance Criteria**:
- User enters pickup and destination addresses in a search bar.
- System displays a list of available drivers within a 5 km radius.
- System provides an estimated time of arrival (ETA) for each driver.
- The interface shows the estimated cost of the trip before booking.
**Priority**: MVP

---

### User Story 2
As a driver, I want to list my available seats so that I can share travel costs with others.
**Acceptance Criteria**:
- Driver sets a specific price per seat and total seats available.
- Driver specifies the departure time, date, and full route details.
- System confirms the listing is visible to passengers in search results.
- Driver can edit or remove the listing before any seat is booked.
**Priority**: MVP

---

### User Story 3
As a user, I want to pay for my ride through the app so that I don't need to carry cash.
**Acceptance Criteria**:
- System supports credit card, debit card, and digital wallet integrations.
- User receives a detailed digital receipt via email immediately after payment.
- Funds are securely held and only transferred to the driver after ride completion.
**Priority**: High

---

### User Story 4
As a passenger, I want to see the driver's rating so that I can feel safe before booking.
**Acceptance Criteria**:
- Ratings are displayed as a numerical value (1-5) and visible stars.
- User can view at least 5 recent written reviews from previous passengers.
- System displays a "Verified" badge for drivers who have completed background checks.
**Priority**: High

---

### User Story 5
As a driver, I want to set a maximum number of passengers so that my car is not overcrowded.
**Acceptance Criteria**:
- Driver selects seat capacity (1-4) from a mandatory dropdown menu.
- System automatically closes the booking once the seat limit is reached.
- Driver can manually see the list of booked passengers in their dashboard.
**Priority**: Medium

---

### User Story 6
As a user, I want to receive real-time notifications about my ride status so that I am always updated.
**Acceptance Criteria**:
- System sends a push notification when a driver accepts a booking.
- A notification is sent when the driver is within 500 meters of the pickup point.
- User receives an SMS alert if the ride is cancelled by the driver.
**Priority**: Medium

---

### User Story 7
As an admin, I want to block users who violate safety rules so that the platform remains secure.
**Acceptance Criteria**:
- Admin can search for users by ID, phone number, or email address.
- Admin must provide a mandatory text reason for blocking the account.
- Blocked users are immediately logged out and cannot create new accounts with the same email.
**Priority**: Low

---

### User Story 8
As a user, I want to see an estimate of the CO2 emissions saved so that I can see my environmental impact.
**Acceptance Criteria**:
- System calculates CO2 savings based on total distance and shared car occupancy.
- Environmental impact is displayed as a graphic on the user's personal profile.
- Users can compare their weekly savings with the average user on the platform.
**Priority**: Low

---

### User Story 9
As a passenger, I want to cancel my ride within a specific timeframe so that I have flexibility.
**Acceptance Criteria**:
- User can cancel the ride for free within 5 minutes of booking confirmation.
- System displays a clear warning about cancellation fees after the grace period.
- The driver receives an instant in-app notification of the cancellation.
**Priority**: High

---

### User Story 10
As a driver, I want to view my trip history so that I can track my earnings over time.
**Acceptance Criteria**:
- System provides a list of all completed trips with dates and earnings.
- Driver can filter the history by week, month, or a custom date range.
- The history includes a summary of the total distance driven and total fuel costs shared.
**Priority**: Medium
