@basic_search
  Feature: Basic search form
    Scenario: T1 - One way flight search - booking.com disabled
      Given As a not logged user navigate to homepage
      When I select one-way trip type
      When Set the departure airport RTM
      And Set the arrival airport MAD
      And Set the departure time 1 week(s) in the future starting from current date
      And Uncheck the 'Check accommodation with booking.com' option
      And Click the search button
      Then I am redirected to the search results page
