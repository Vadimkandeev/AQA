from constans import BASE_URL, INVALID_BASE_URL


def test_create_booking(auth_session, booking_data, patch_booking_data):
    response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert  response.status_code == 200

    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    #Проверяем получение
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.status_code == 200


    #Изменяем бронь (Patch)
    get_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_booking_data)
    assert get_booking.status_code == 200
    # Проверяем изменения
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.json()['firstname'] == patch_booking_data['firstname']
    assert get_booking.status_code == 200

    #Обновляем бронь (Put)
    get_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
    assert get_booking.status_code == 200
    # Проверяем изменения
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.json()['firstname'] == booking_data['firstname']
    assert get_booking.status_code == 200


    #Удаляем
    delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert delete_booking.status_code == 201

    #Проверка удаления
    get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_booking.status_code == 404



# Негативные проверки

def test_negative(auth_session, booking_data):
    pass
