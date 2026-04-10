from constans import BASE_URL


def test_create_booking(auth_session, booking_data):
    response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert  response.status_code == 200

    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    #Проверяем получение
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.status_code == 200

    #Удаляем
    delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert delete_booking.status_code == 201

    #Проверка удаления
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.status_code == 404
