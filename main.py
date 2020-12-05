def parse_parameters(query: str) -> dict:
    return {}


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':

    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
        assert parse_parameters('https://mail.google.com/mail/u/0/?tab=rm') == {'tab': 'rm'}
    assert parse_parameters(
        'https://www.google.com/search?q=telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%8B&oq=telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB&aqs=chrome.0.0i433j69i57j0l6.9788j0j7&sourceid=chrome&ie=UTF-8') == \
           {'q': 'telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%8B',
            'oq': 'telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB',
            'aqs': 'chrome.0.0i433j69i57j0l6.9788j0j7',
            'sourceid': 'chrome',
            'ie': 'UTF-8'}
    assert parse_parameters(
        'https://rozetka.com.ua/?gclid=CjwKCAjw0On8BRAgEiwAincsHPoy20JoXn1-U8KFRsx3JH9siOtxoXQsWIel6KvI4MU9chAipecK6RoCO0EQAvD_BwE') == \
           {'gclid': 'CjwKCAjw0On8BRAgEiwAincsHPoy20JoXn1-U8KFRsx3JH9siOtxoXQsWIel6KvI4MU9chAipecK6RoCO0EQAvD_BwE'}
    assert parse_parameters('https://www.youtube.com/watch?v=o3zIjodedhA&ab_channel=XYZ') == {'v': 'o3zIjodedhA',
                                                                                              'ab_channel': 'XYZ'}
    assert parse_parameters('https://www.youtube.com/watch?v=XwpHbbXZvXA&ab_channel=ZProger%5BIT%5D') == {
        'v': 'XwpHbbXZvXA',
        'ab_channel': 'ZProger%5BIT%5D'}
    assert parse_parameters('https://www.youtube.com/watch?v=0oBi8OmjLIg&ab_channel=JomaTech') == {'v': '0oBi8OmjLIg',
                                                                                                   'ab_channel': 'JomaTech'}
    assert parse_parameters('https://www.youtube.com/watch?v=XZmGGAbHqa0&ab_channel=GoogleWorkspace') == {
        'v': 'XZmGGAbHqa0',
        'ab_channel': 'GoogleWorkspace'}
    assert parse_parameters('https://www.youtube.com/watch?v=ZBimwHa2FPY&ab_channel=WebForMySelf') == {
        'v': 'ZBimwHa2FPY',
        'ab_channel': 'WebForMySelf'}


    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
