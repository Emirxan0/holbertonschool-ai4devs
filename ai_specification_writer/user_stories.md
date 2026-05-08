# User Stories

### User Story 1
As a passenger, I want to search for nearby drivers so that I can find a quick ride.
**Acceptance Criteria**:
- User enters pickup and destination addresses.
- System displays available drivers within a 5 km radius.
- System provides an estimated time of arrival for each driver.
**Priority**: MVP

---

### User Story 2
As a driver, I want to list my available seats so that I can share travel costs with others.
**Acceptance Criteria**:
- Driver sets a specific price per seat.
- Driver specifies the departure time, date, and full route.
- System confirms the listing is visible to passengers in the search results.
**Priority**: MVP

---

### User Story 3
As a user, I want to pay for my ride through the app so that I don't need to carry cash.
**Acceptance Criteria**:
- System supports credit card, debit card, and digital wallets.
- User receives a detailed digital receipt via email after payment.
- Funds are only transferred to the driver after the ride is marked as completed.
**Priority**: High

---

### User Story 4
As a passenger, I want to see the driver's rating so that I can feel safe before booking.
**Acceptance Criteria**:
- Ratings are displayed as a numerical value and stars (1-5).
- User can view the last 5 written reviews from other passengers.
- System highlights drivers with "Top Rated" badges if they have over 4.8 stars.
**Priority**: High

---

### User Story 5
As a driver, I want to set a maximum number of passengers so that my car is not overcrowded.
**Acceptance Criteria**:
- Driver selects capacity from a dropdown menu (1-4 seats).
- System prevents further bookings automatically once the seat limit is reached.
- Driver can update the number of available seats in real-time before the trip starts.
**Priority**: Medium

---

### User Story 6
As a user, I want to receive real-time notifications about my ride status so that I am always updated.
**Acceptance Criteria**:
- System sends a push notification when a booking is confirmed.
- Notification is triggered when the driver is exactly 2 minutes away from pickup.
- User receives an alert if the driver cancels the trip.
**Priority**: Medium

---

### User Story 7
As an admin, I want to block users who violate safety rules so that the platform remains secure.
**Acceptance Criteria**:
- Admin can search for any user by their unique ID, phone number, or email.
- Admin must provide a mandatory reason for the block in a text field.
- Blocked users are immediately logged out and prevented from signing in again.
**Priority**: Low

---

### User Story 8
As a user, I want to see an estimate of the CO2 emissions saved so that I can see my environmental impact.
**Acceptance Criteria**:
- System calculates CO2 savings based on the total trip distance shared.
- The environmental impact is displayed prominently on the user's dashboard.
- Users can share their total "Green Points" on social media platforms.
**Priority**: Low

---

### User Story 9
As a passenger, I want to cancel my ride within a certain timeframe so that I have flexibility if my plans change.
**Acceptance Criteria**:
- User can cancel for free within 5 minutes of booking.
- System displays a warning message about potential fees after the grace period.
- Driver is notified instantly when a passenger cancels.
**Priority**: High
