# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "شكرا لاختيارك لنا ، أنا اتصل بك اليوم بخصوص طلبك للحصول على عرض أسعار / أسعار لـ (نيسان باترول)"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

#

class WelcomIntenttHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("WelcomIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "لدينا فئات نيسان وهي ثلاث فئات…  1: الفل.. 2: نصف الفل..  3: الستاندر)..  أي منها تحتاج..  إلى مزيد من المعلومات الرجاء الرد باسم الفئة.. فل او نصف فل او الستاندر"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class ElfolIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ElfolIntent")(handler_input)

    def handle(self, handler_input):
        speak_output1 = "هل تريد السيارة على نظام الشراء النقد ام التأجير ام تجربة القياده "
        speak_output2 = "الرجاء الرد ب شراء نقدا ام تاجير ام تجربه"
        speak_output = speak_output1 + speak_output2
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CashIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("CashIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = " تتوفر الينا الفئة بالالوان الاتية (الاسود – الابيض - الذهبي) اي الالوان تفضل الرجاء الرد باختيار اللون"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class BlackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BlackIntent")(handler_input)

    def handle(self, handler_input):
        speak_output1 = " ، سأقوم بتحويل طلبك إلى في صالة العرض وسيتصل بك بخصوص توفر اللون ويكمل معك باقي الاجرائات"
        speak_output2 = "هل تريد خدمة اخرى ؟"
        speak_output = speak_output1 + speak_output2
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class RentalIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RentalIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "هل يمكنك أن تخبرنا من فضلك عن أي بنك تريد المتابعة الرجاء الرد باسم البنك؟"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RajhiBankIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RajhiBankIntent")(handler_input)

    def handle(self, handler_input):
        speak_output1 = ": سأقوم بتحويل طلبك إلى مندوب المبيعات وسوف يتصل بك ويبلغك بالحسابات كامله"
        speak_output2 = "هل لديك اي التزامات الرجاء الرد بنعم لدى التزامات ام لا ليس لدى التزامات…"
        speak_output  = speak_output1 + speak_output2
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class ResposibilityIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ResposibilityIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "هل الالتزام عالي ام منخفض الرجاء الرد ب الالتزام عالي ام الالتزام  منخفض"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class HighIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("HighIntent")(handler_input)

    def handle(self, handler_input):
        speak_output1 = "يؤسفني إبلاغك ... بأن التزاماتك مرتفعة وفي هذه الحالة سيرفض البنك طلبك للتأجير"
        speak_output2 = "هل تريد خدمه اخرى ؟ الرجاء الرد ب نعم ام لا      "
        speak_output  = speak_output1 + speak_output2
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class LowIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LowIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "هل تحب تجربة السيارة الرجاء الرد بنعم اريد تجربة السياره ام لا اريد تجربة السياره"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class YesCarIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("YesCarIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = " هل لديك رخصة قيادة سارية الرجاء الرد بنعم لدى رخصة قياده ساريه ام لايوجد رخصة قياده ساريه"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class YesLicenceIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("YesLicenceIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "سوف يتم التواصل معك لاحقا لتحديد الموعد لتجربة القيادة"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class NoLicenceIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NoLicenceIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "نعتذر عزيز العميل عن عدم اكمال الاجراءات لعدم توفر رخصة سارية المفعول"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NoServiceIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NoServiceIntent")(handler_input)

    def handle(self, handler_input):
        speak_output =  "شكرا لاستخدامك لنا "
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
#--------------------------------------------------------------------------------------------------------------------

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "مع السلامه"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = " الرجاء قم باعادة الاجابة بالاختيار الصحيح"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = " الرجاء قم باعادة الاجابة بالاختيار الصحيح"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(WelcomIntenttHandler())
sb.add_request_handler(ElfolIntentHandler())
sb.add_request_handler(CashIntentHandler())
sb.add_request_handler(BlackIntentHandler())
sb.add_request_handler(RentalIntentHandler())
sb.add_request_handler(RajhiBankIntentHandler())
sb.add_request_handler(ResposibilityIntentHandler())
sb.add_request_handler(HighIntentHandler())
sb.add_request_handler(LowIntentHandler())
sb.add_request_handler(YesCarIntentHandler())
sb.add_request_handler(YesLicenceIntentHandler())
sb.add_request_handler(NoLicenceIntentHandler())
sb.add_request_handler(NoServiceIntentHandler())



sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()