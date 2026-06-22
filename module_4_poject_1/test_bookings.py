from constans import BASE_URL, ENDPOINT
from custom_requester import CustomRequester


def test_create_booking(auth_session, booking_data, patch_booking_data, put_booking_data):

    #*************************************************************************
    requester = CustomRequester(auth_session, BASE_URL)

    response = requester.send_request("POST", ENDPOINT, booking_data, 200, True)
    #*************************************************************************

    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    #Проверяем получение
    url = f"{ENDPOINT}/{booking_id}"
    requester.send_request("GET", url, None, 200, True)



    #Изменяем бронь (Patch)
    requester.send_request("PATCH", url, patch_booking_data, 200, True)

    # Проверяем изменения
    get_booking = requester.send_request("GET", url, None, 200, True)
    assert get_booking.json()['firstname'] == patch_booking_data['firstname']


    #Обновляем бронь (Put)
    #get_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=put_booking_data)
    requester.send_request("PUT", url, put_booking_data, 200, True)

    # Проверяем изменения
    get_booking = requester.send_request("GET", url, None, 200, True)
    assert get_booking.json()['firstname'] == put_booking_data['firstname']



    #Удаляем
    requester.send_request("DELETE", url, None, 201, True)


    #Проверка удаления
    requester.send_request("GET", url, None, 404, True)




# Негативные проверки-----------------------------------------------

def test_negative(auth_session, booking_data, patch_booking_data, invalid_type_booking_data, empty_booking_data, \
                  no_required_field_booking_data, non_exist_field_booking_data, put_booking_data):


    admin_session = auth_session

    requester = CustomRequester(admin_session, BASE_URL)

    response = requester.send_request("POST", ENDPOINT, booking_data, 200, True)


    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    url = f"{ENDPOINT}/{booking_id}"


    # Негативные проверки GET
    invalid_url = f"{ENDPOINT}/{99999999999}"
    requester.send_request("GET", invalid_url, None, 404, True)

    # Негативные проверки POST
    # Отсутствует обязательное поле
    requester.send_request("POST", ENDPOINT, no_required_field_booking_data, 500, True)

    # Пустое тело запроса
    requester.send_request("POST", ENDPOINT, empty_booking_data, 500, True)

    # Негативные проверки PUT
    # Несуществующий ресурс
    requester.send_request("PUT", invalid_url, put_booking_data, 405, True)

    # Отсутствует обязательное поле
    auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=no_required_field_booking_data)

    # Негативные проверки PATCH
    # Несуществующее поле
    response = requester.send_request("PATCH", url, non_exist_field_booking_data, 200, True)
    assert "may_flavor" not in response.json()

    # Неверный тип данных
    requester.send_request("PATCH", url, invalid_type_booking_data, 200, True)

    # Удаляем
    requester.send_request("DELETE", url, None, 201, True)








