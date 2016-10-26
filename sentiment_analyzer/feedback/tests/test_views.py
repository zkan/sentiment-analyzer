from django.core.urlresolvers import reverse
from django.test import TestCase


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.url = reverse('feedback')

    def test_access_feedback_index_page(self):
        response = self.client.get(self.url)

        expected = '<h1>Feedback</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_have_feedback_table(self):
        response = self.client.get(self.url)

        expected = '<th>Message</th>'
        expected += '<th>Predicted</th>'
        self.assertContains(response, expected, status_code=200)