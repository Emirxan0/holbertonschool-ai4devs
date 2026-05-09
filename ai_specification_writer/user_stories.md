# User Stories

### User Story 1
As a passenger, I want to search for nearby drivers so that I can find a quick ride.
**Acceptance Criteria**:
- User enters pickup and destination addresses in a search bar.
- System displays a list of available drivers within a 5 km radius.
- System provides an estimated time of arrival (ETA) for each driver.
**Priority**: MVP

---

### User Story 2
As a driver, I want to list my available seats so that I can share travel costs with others.
**Acceptance Criteria**:
- Driver sets a specific price per seat and total seats available.
- Driver specifies the departure time, date, and full route details.
- System confirms the listing is visible to passengers in search results.
**Priority**: MVP

---

### User Story 3
As a user, I want to pay for my ride through the app so that I don't need to carry cash.
**Acceptance Criteria**:
- System supports credit card, debit card, and digital wallet integrations.
- User receives a detailed digital receipt via email immediately after payment.
- Funds are only transferred to the driver after ride completion.
**Priority**: High

---

### User Story 4
As a passenger, I want to see the driver's rating so that I can feel safe before booking.
**Acceptance Criteria**:
- Ratings are displayed as a numerical value (1-5) and visible stars.
- User can view at least 5 recent written reviews from previous passengers.
- System displays a "Verified" badge for drivers with background checks.
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
- A notification is sent when the driver is within 500 meters of the pickup.
- User receives an SMS alert if the ride is cancelled by the driver.
**Priority**: Medium

---

### User Story 7
As an admin, I want to block users who violate safety rules so that the platform remains secure.
**Acceptance Criteria**:
- Admin can search for users by ID, phone number, or email address.
- Admin must provide a mandatory text reason for blocking the account.
- Blocked users are immediately logged out and cannot sign in.
**Priority**: Low

---

### User Story 8
As a user, I want to see an estimate of the CO2 emissions saved so that I can see my environmental impact.
**Acceptance Criteria**:
- System calculates CO2 savings based on distance and shared occupancy.
- Environmental impact is displayed as a graphic on the user's profile.
- Users can share their total savings on social media platforms.
**Priority**: Low
