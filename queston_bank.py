import os
import random
from dataclasses import dataclass
from typing import Literal


# --- Question/Answer structure ---
@dataclass
class QA:
    id: int
    question: str
    choices: str
    answer: str
    answer_type: Literal["single", "multiple", "true_false"] = "single"
    comment_hint: str = ""
    link_pic: str = ""


class QuestionBank:
    start_path = os.path.dirname(__file__)

    @classmethod
    def get_random(cls):
        return random.choice(cls.questions)

    @classmethod
    def get_random_in_range(cls, lower: int, upper: int):
        """Return a random QA object where id is between lower and upper (inclusive)."""
        candidates = [q for q in cls.questions if lower <= q.id <= upper]
        if not candidates:
            raise ValueError(f"No questions found in range {lower}-{upper}")
        return random.choice(candidates)

    questions = [
        QA(
            id=1,
            question="Which of the following tasks is not performed by the Exchange Council?",
            choices="""
            1. Adoption of the Exchange Rules
            2. Supervision of the management board
            3. Appointment of the head of the Trading Surveillance Office
            4. Admission of securities
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=2,
            question="Which exchange body decides on the commencement, suspension, interruption and discontinuation of the price fixing for securities?",
            choices="""
            1. Cash Markets Operations
            2. Trading Surveillance Office
            3. Management Board of the Exchange
            4. Exchange Council
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=3,
            question="For which of the following functions is the Management Board of the Exchange responsible?",
            choices="""
            1. Monitoring of exchange trading as the implementing body of the Supervisory Authority
            2. Definition of start and end of price determination
            3. Brokerage of exchange transactions
            4. Prosecution of insider trading violations
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=4,
            question="Which German law requires every exchange to establish and operate a Trading Surveillance Office?",
            choices="""
            1. German Securities Trading Act
            2. German Banking Act
            3. German Exchange Act
            4. German Exchange Supervisory Act
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=5,
            question="The Exchange Rules stipulate that companies must provide sufficient collateral for the performance of their transactions. Which body is responsible for monitoring compliance with the security framework of individual trading participants?",
            choices="""
            1. Management Board of the Exchange
            2. Trading Surveillance Office
            3. German Federal Financial Supervisory Authority (BaFin)
            4. Exchange Supervisory Authority
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=6,
            question="Which of the following measures is not available to the Disciplinary Committee to take action against a trading participant?",
            choices="""
            1. Reprimand
            2. Fine of up to €1,000,000
            3. Suspension from the exchange for up to 30 trading days
            4. Irrevocable withdrawal of the trading license
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=7,
            question="The claims and/or liabilities with respect to the trading of certain securities (as determined by Management Board) are clearing via a central counterparty.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=8,
            question="The central counterparty for transactions in CCP-eligible securities is Deutsche Börse AG.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            the Deutsche Börse AG is the parent company and the organizing institution of the Frankfurt Stock Exchange 
            (which operates Xetra), but it is not the Central Counterparty (CCP) itself.
            """
        ),
        QA(
            id=9,
            question="Settlement for trades concluded on FWB is done in principle via Clearstream Banking AG or via another central securities depository recognised in the Exchange Rules.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=10,
            question="When will trading on the FWB be suspended in the regulated market pursuant to section 59 of the Exchange Rules?",
            choices="""
            1. If orderly settlement is temporarily at risk.
            2. On the day before the annual financial statement of a stock corporation is released.
            3. If it is deemed necessary in order to protect investors.
            4. On the day of the stock corporation's annual general meeting.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=11,
            question="Who must the Management Board inform immediately if trading in the regulated market is suspended?",
            choices="""
            1. The Trading Surveillance Office and the Exchange Supervisory Authority
            2. The German Federal Financial Supervisory Authority (BaFin) and the Exchange Supervisory Authority
            3. The Exchange Council and the Trading Surveillance Office
            4. The Exchange Supervisory Authority and the Exchange Council
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=12,
            question="Which statement is wrong?",
            choices="""
            1. If trading in the regulated market is suspended by the Management Board existing orders are deleted.
            2. Suspension of trading may be limited to parts of trading.
            3. Suspension of trading cannot be limited to parts of trading.
            4. If trading in the regulated market is interrupted by the Management Board existing orders are not deleted.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=13,
            question="What is prohibited according to the market integrity clause (section 121 Exchange Rules)?",
            choices="""
            1. Concluding OTC trades.
            2. Placing orders in accordance with the common market practice.
            3. Effect a price which is not in line with the market or an artificial price level in the Exchange EDP.
            4. None of the above.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=14,
            question="Which of the following circumstances does violate the market integrity clause (section 121 Exchange Rules)?",
            choices="""
            1. Causing an artificial price level.
            2. Entering orders that are suitable to erroneously or deceptively influence offer and demand in a security.
            3. Influencing the price of a security due to orders of one trading participant.
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=15,
            question="Which statement applies to the short code regime?",
            choices="""
            1. When entering an order, the short code assigned to the long code of the order must be entered.
            2. As a general rule, only one short code can be assigned to a long code.
            3. When a short code is used for the first time, FWB must be notified of the assigned long code by the end of the trading day following the trading day on which the short code was first used.
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=16,
            question="Which statement is not correct in case of technical problems?",
            choices="""
            1. In the event of blocking the access to the exchange EDP for all companies, no more entries can be effected (halt status).
            2. If the trading system of a company is non-functional, the Management Board may, upon request, enter data into the exchange EDP on behalf of such trading participant.
            3. A breakdown of the telephone system or another failure which prevents a communication via telephone shall immediately be made known to the Management Board by the company or the concerned exchange trader.
            4. Trading Surveillance Office can block the access to the exchange EDP for one, several or all companies.
            """,
            answer="4",
            answer_type="single",
            comment_hint="""
            The Trading Surveillance Office (TSO) is primarily responsible for monitoring trading activities to ensure compliance with exchange rules and regulations. 
            While the TSO has significant authority in overseeing market integrity, it does not have the authority to block access to the exchange EDP (Electronic Data Processing system) for trading participants.
            """
        ),
        QA(
            id=17,
            question="When can the Management Board block the access to the exchange EDP?",
            choices="""
            1. In case of technical problems.
            2. If orderly exchange trading is endangered.
            3. As a rule, the access to the trading system cannot be locked.
            4. None of the above.
            """,
            answer="1",
            answer_type="single",
            comment_hint="""
            The Management Board of the Exchange has the authority to block access to the exchange EDP (Electronic Data Processing system) in case of technical problems.
            This measure is taken to ensure the integrity and orderly functioning of the exchange trading system.   
            """
        ),
        QA(
            id=18,
            question='How does a trading participant legitimise "Trading on Behalf" if individual orders or quotes are to be deleted in the event of technical problems?',
            choices="""
            1. By mentioning a personal identification number.
            2. Via a recall by employees of Cash Markets Operations.
            3. By mentioning an active user ID.
            4. By mentioning the system password.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=19,
            question="When does the quote provider for a structured product not have to specify an ask limit in its indicative quote for the specialist?",
            choices="""
            1. When the security is completely sold out by the issuer (sold-out status).
            2. If the security has been terminated by the issuer.
            3. When the market is sufficiently liquid.
            4. If the security is affected by a legal amendment in such a way that a purchase of the security is no longer possible.
            """,
            answer=["1", "2", "4"],
            answer_type="multiple",
            comment_hint="""
            A quote provider for a structured product is generally required to provide both bid and ask limits in its indicative quotes to ensure market liquidity and transparency.
            However, there are specific situations where the quote provider is exempt from specifying an ask limit:

            1. Sold-out status: If the security is completely sold out by the issuer, there is no availability for purchase, and thus no need to provide an ask limit.
            2. Termination by the issuer: If the security has been terminated by the issuer, it is no longer available for trading, and therefore, an ask limit is not applicable.
            3. Legal amendments: If the security is affected by a legal amendment that makes purchasing the security impossible, the quote provider is not required to provide an ask limit.
            
            The third option, "When the market is sufficiently liquid," is not a valid reason for omitting the ask limit, as liquidity does not negate the requirement for both bid and ask limits in indicative quotes.
            """,
        ),
        QA(
            id=20,
            question="Which of the following obligations must quote providers fulfil in trading with structured products?",
            choices="""
            1. The indicative quote which they make available to the specialists must always have a bid and an ask limit.
            2. They must provide the specialist with at least one indicative quote on each trading day.
            3. They must provide the Management Board with an expert contact person who is admitted for the company as an exchange trader at the FWB and a technical contact person.
            4. They shall name a binding quote to the specialist upon their request.
            """,
            answer=["2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=21,
            question="What are the specific rules applicable to structured products in the Continuous Auction?",
            choices="""
            1. Short sales are not permitted.
            2. The issuer must name a quote provider for the respective security in the application for introduction to trading.
            3. The quote provider must submit indicative quotes with bid and ask limits in every situation.
            4. The Trading Surveillance Office may interdict quote providers the quotation in whole or in part.
            """,
            answer=["1", "2"],
            answer_type="multiple",
        ),
        QA(
            id=22,
            question="Who determines the quote provider for a structured product?",
            choices="""
            1. Issuer
            2. Trading Surveillance Office
            3. Specialist
            4. Management Board of the Exchange
            """,
            answer="1",
            answer_type="single",
        ),
        QA(
            id=23,
            question="Which of the following statements does not apply to quote providers for structured products?",
            choices="""
            1. They must be available by telephone to the Management Board of the Exchange and the Specialists from one hour before the start of trading until one hour after the end of electronic trading.
            2. They shall ensure that the necessary human, technical and financial resources are available to meet the quote requirement.
            3. They must be identical with the issuer.
            4. They need an expert contact person who is admitted for the company as exchange trader at the FWB.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=24,
            question="In the case of quote restrictions for a structured product, what applies to the quote providers?",
            choices="""
            1. They must indicate this immediately by a quotation with a bid and ask limit of "0".
            2. If the reason is a system failure, they can inform the Management Board and the Trading Surveillance Office in writing in addition to the quotation with "0".
            3. At the request of the Management Board or the Trading Surveillance Office, they shall provide information on the reason for and the expected duration of the quote restrictions.
            4. All the answers are correct.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=25,
            question="For Exchange transactions due for settlement the seller is obligated to pay the corresponding cash amount for the securities.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            In exchange transactions due for settlement, the seller is obligated to deliver the securities to the buyer, while the buyer is obligated to pay the corresponding cash amount for the securities.
            This means that the payment obligation lies with the buyer, not the seller.
            """,
        ),
        QA(
            id=26,
            question="For Exchange transactions due for settlement the buyer is obligated to pay the corresponding cash amount for the securities earliest on the third day after trade conclusion.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=27,
            question="Exchange transactions in shares must be settled on the second performance day after the trade day.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=28,
            question="Which statements are correct for pre-arranged trades according to section 3 of the Conditions for Transactions on the FWB?",
            choices="""
            1. During continous trading (trading model continuous trading with intraday auctions) they are admissible if one of the participants, prior to entering his/her order, has enterted an appropriate trade request.
            2. During continuous trading (trading model continuous trading with intraday auctions) they are always forbidden.
            3. The order leading to the pre-arranged trade must be entered earliest 5 seconds and latest 35 seconds after the trade request.
            4. None of the above
            """,
            answer=["1", "3"],
            answer_type="multiple",
            comment_hint="""
            Based on the search results, pre-arranged trades are a specific type of trade that requires a "Trade Request" to be entered beforehand. This is an exception to the general rule that prevents two parties from entering orders that would immediately execute against each other.

            The relevant rules state:

            Pre-arranged trades are admissible during continuous trading if a participant first enters an appropriate trade request.

            The order leading to the trade must be entered a specific timeframe after the trade request. 
            The search results state "onefive seconds at the earliest and 12135 seconds at the latest" in one document, and "5 seconds at the earliest and 35 seconds at the latest" in another. 
            The latter seems to be the most updated, or at least a common rule.
            """,
        ),
        QA(
            id=29,
            question="Which of the following circumstances violate section 3 of the Conditions for Transactions on the FWB?",
            choices="""
            1. The entry of opposite orders concerning the same security and executable immediately by several traders of one company.
            2. A knowing cross trade without trade request before.
            3. A pre-arranged trade without trade request before.
            4. The entry of orders with the intention of influencing the price of derivatives relating to the security in question that are traded on Eurex Deutschland.
            """,
            answer=["2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=30,
            question="When is a cross trade or a pre-arranged trade permitted according to section 3 of the Conditions for Transactions on the FWB?",
            choices="""
            1. If one of the involved traders had entered a trade request in continuous trading (trading model continuous trading with intraday auctions) before.
            2. If the order leading to the cross trade or pre-arranged trade had been entered earliest 5 seconds and latest 35 seconds after the trade request.
            3. If one of the involved traders had announced the cross trade or pre-arranged trade to trading surveillance office.
            4. If the phase crossing is active in the trading system.
            """,
            answer=["1", "2"],
            answer_type="multiple",
            comment_hint="""
            The first statement is correct: 
            a trade request must be entered in the continuous trading model before the order.
            The second statement is also correct: 
            the subsequent order must be entered within a specific time window, which is earliest 5 seconds and latest 35 seconds after the trade request.
            The third statement, about announcing the trade to the trading surveillance office, is not a requirement for permitting the trade itself. The rules focus on the automated process via the trading system.
            The fourth statement is not a recognized condition for permitting these types of trades.
            """,
        ),
        QA(
            id=31,
            question="Which statements are correct for cross trades?",
            choices="""
            1. During continuous trading (trading model continuous trading with intraday auctions) they are always forbidden.
            2. If the self match prevention function is used by a trading participant, unintended crossings during continuous trading (trading model continuous trading with intraday auctions) and during Trade-at-Close are prevented by the trading system.
            3. During continous trading (trading model continuous trading with intraday auctions) they are admissible if one of the participants, prior to entering his/her order, has enterted an appropriate trade request.
            4. None of the above
            """,
            answer=["2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=32,
            question="Which details must a trade request contain?",
            choices="""
            1. Trader ID
            2. Quantity
            3. Limit
            4. Security
            """,
            answer=["2", "4"],
            answer_type="multiple",
            comment_hint="""
            A trade request must contain the quantity and the security.
            The trader ID and limit are not required details for a trade request.
            this is because the trade request is primarily used to signal the intention to enter a trade, 
            and the specific details of the trade (like trader ID and limit) are typically provided when the actual order is entered following the trade request.
            """,
        ),
        QA(
            id=33,
            question="Cross-Trades and Pre-Arranged Trades ...",
            choices="""
            1. are admissible during continuous trading (trading model continuous trading with intraday auctions) if they have been announced by a trade request and the deadline of order entry has been met.
            2. are possible in auctions and volatility interruptions.
            3. are always forbidden.
            4. can be entered into the system anytime.
            """,
            answer=["1", "2"],
            answer_type="multiple",
        ),
        QA(
            id=34,
            question="Which deadline must be considered in connection with a mistrade application?",
            choices="""
            1. In case of securities traded in Continuous Trading with intra-day auctions or in auctions, the Mistrade application shall be submitted within three trading hours upon receipt of the execution confirmation.
            2. In case of securities traded in Continuous Auction, the Mistrade application shall be submitted within one trading hour upon receipt of the execution confirmation.
            3. In case of trades in securities traded in Continuous Auction, the Mistrade application shall be submitted within two trading hours upon receipt of the execution confirmation.
            4. In case of securities traded in Continuous Trading with intra-day auctions or in auctions, the Mistrade application shall be submitted within ten minutes upon receipt of the execution confirmation.
            """,
            answer=["3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=35,
            question="Under which circumstances can the Management Board cancel a transaction?",
            choices="""
            1. The price of the transaction in question is not in line with market conditions.
            2. The price of the transaction in question is in line with market conditions.
            3. An admissible application was submitted
            4. The involved parties reach an agreement without involving the Exchange and notify the Exchange within 24 hours.
            """,
            answer=["1", "3"],
            answer_type="multiple",
        ),
        QA(
            id=36,
            question="Which details must a mistrade application contain?",
            choices="""
            1. Company and contact person of the applicant
            2. Time, volume and price of transaction
            3. Details regarding the price in line with the market
            4. Company and contact person of the counterparty
            """,
            answer=["1", "2", "3"],
            answer_type="multiple",
            comment_hint="""
            A mistrade application must contain all the details necessary to identify the trade and the parties involved, 
            as well as the justification for why it should be considered a mistrade. 
            This includes the applicant's details, the transaction's specifics (time, volume, price), and information demonstrating the price was not in line with the market.
            """

        ),
        QA(
            id=37,
            question="If a bilateral trade in a security that has its main trading venue outside the EU is not fulfilled in time, the buyer is entitled to self-execution. Which of the following tasks does not have to be fulfilled in the context of self-execution?",
            choices="""
            1. Setting of a reasonable period for performance.
            2. To purchase the undelivered securities after expiry of a grace period.
            3. Inform the CSD of the late delivery.
            4. To sell the undelivered securities after expiry of a grace period.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=38,
            question="Which statement regarding the conclusion, performance or overdue performance of exchange transactions is false?",
            choices="""
            1. Exchange transactions are to be settled at the earliest two performance days after conclusion of the transaction.
            2. Exchange transactions are concluded between the admitted companies or between them and a central counterparty.
            3. The right to self-execution also applies to cleared transactions.
            4. Counterparties involved in a transaction receive an electronic execution confirmation.
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            Think about who is the actual counterparty for cleared transactions and what "self-execution" means. 
            The clearing house (CCP) guarantees the trade, so the original parties no longer have a claim against each other. 
            Self Execution cannot be cleared. 
            The two concepts are mutually exclusive.
            """
        ),
        QA(
            id=39,
            question="What applies if an exchange transaction is not settled in time?",
            choices="""
            1. For bilateral transactions in securities having their main trading venue in the EU, the relevant articles of the Central Securities Depository Regulation (CSDR) apply.
            2. For cleared transactions, the clearing conditions of the clearing house apply.
            3. In the case of bilateral transactions not covered by the CSDR, the non-defaulting party is entitled to self-execution.
            4. All answers are correct.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=40,
            question="Which statement regarding the T7 Entry Service (TES) is correct?",
            choices="""
            1. For trades concluded via the TES, volume and price can be arranged as required.
            2. The trading participant shall specify a minimum volume for its off-book trades.
            3. Trades can only be concluded if the price is within a defined range.
            4. The TES order functionality can only be used by admitted exchange traders.
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            The T7 Entry Service (TES) is a platform that allows trading participants to enter off-book trades.
            One of the key features of TES is that trades can only be concluded if the price is within a defined range.
            This ensures that the trades are executed at fair market prices and helps maintain market integrity.
            """,
        ),
        QA(
            id=41,
            question="When is an off-book trade prohibited?",
            choices="""
            1. If the trade was entered into the system by mistake.
            2. If the beneficial owner is identical on the purchase and sale side.
            3. If the trade has not been confirmed by the end of the off-book trading period.
            4. If the trade was entered by an employee of the trading participant who is not admitted to trading.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=42,
            question="Which statement is correct for the request-for-quote functionality Xetra EnLight?",
            choices="""
            1. Requesters (traders) may request offers to purchase or sell a certain amount of a security directly from one or more responders (market makers).
            2. Offers may only be made and accepted within a timeframe determined by the management board of FWB.
            3. If several responders submit a Xetra EnLight offer, the requester may only accept one Xetra EnLight offer.
            4. All answers are correct.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=43,
            question="Which of the following statements is not applicable for trading funds (w/o ETFs) in Continuous Auction?",
            choices="""
            1. The quotation of the Specialist shall be made on the basis of the current order book situation and the price of the funds calculated by the Specialists.
            2. In the event of special situations, such as the suspension of issuance or repurchase of fund units by the issuer, the specialist must immediately inform the Management Board and the Trading Surveillance Office of the FWB in writing.
            3. The quotation of the specialist is based exclusively on the current order book situation.
            4. In particular, the Management Board may suspend trading in the relevant fund units in the event of a suspension of the repurchase of fund units or the closure of a fund.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=44,
            question="Where are the tasks for the specialists in trading funds (w/o ETFs) in addition to the Exchange rules regulated?",
            choices="""
            1. In the trading regulation for the Regulated Unofficial Market on Frankfurter Wertpapierbörse (FWB).
            2. In the general terms and conditions for Xetra.
            3. In the conditions for transactions on the Frankfurter Wertpapierbörse (FWB).
            4. None of the above.
            """,
            answer="1",
            answer_type="single",
        ),
        QA(
            id=45,
            question="Which statement regarding the quotation duty of specialists in trading funds (w/o ETFs) is correct?",
            choices="""
            1. If the issuer suspends the issue of fund units, the specialist is exempted from the obligation to quote on the ask side.
            2. If the issuer suspends the issue of fund units, the specialist is exempted from the obligation to quote on the bid side.
            3. If the repurchase of fund units by the issuer is suspended, the specialist is obliged to provide indicative quotes.
            4. During trading hours, binding quotes must be submitted on an ongoing basis.
            """,
            answer="1",
            answer_type="single",
        ),
        QA(
            id=46,
            question="Which fundamental principles apply to the Xetra market model?",
            choices="""
            1. There is post-trade anonymity due to the presence of a central counterparty.
            2. In the context of pre-trade anonymity, trading participants do not see the identity of the order submitter in the open order book.
            3. During Trade-at-Close the order book is open.
            4. In principle, the order book is closed.
            """,
            answer=["1", "2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=47,
            question="Which of the following statements are valid for continuous trading in connection with auctions?",
            choices="""
            1. An ISIN (a security) can be traded in several trading currencies as a dedicated single instrument, i.e. an instrument refers to a specific ISIN currency combination.
            2. In opening auctions also fractions are supported.
            3. Auctions are only called when required.
            4. During the call phase the order book is partially closed.
            """,
            answer=["1", "4"],
            answer_type="multiple",
        ),
        QA(
            id=48,
            question="Which statements are valid for continuous trading in connection with auctions?",
            choices="""
            1. The trading model is order driven.
            2. Orders are executed according to price/time priority.
            3. Trading of fractions is supported.
            4. Trading is anonymous.
            """,
            answer=["1", "2", "4"],
            answer_type="multiple",
            comment_hint="""
            Partials (fills of whole shares) are allowed, but Fractions (of shares) are not supported
            """,
        ),
        QA(
            id=49,
            question="Which securities are tradeable in the trading model continuous trading in connection with auctions?",
            choices="""
            1. All securities listed at FWB.
            2. Selected shares, bonds, Exchange Traded Funds and Exchange Traded Products.
            3. Selected shares, Exchange Traded Funds and Exchange Traded Products.
            4. None of the above.
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            The trading model continuous trading in connection with auctions on the Xetra platform is designed to facilitate
            the trading of selected shares, Exchange Traded Funds (ETFs), and Exchange Traded Products (ETPs).
            This model does not encompass all securities listed at FWB, nor does it include bonds.
            Therefore, the correct answer is that it includes selected shares, Exchange Traded Funds, and Exchange Traded Products.
            """,
        ),
        QA(
            id=50,
            question="Which statement is correct for the trading venue Xetra?",
            choices="""
            1. Three hierarchy levels of traders are distinguished.
            2. Information users without trader admission are possible.
            3. Traders can be organized in trader groups.
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=51,
            question="In the trading model continuous trading in connection with auctions a trader can act as ...",
            choices="""
            1. Issuer.
            2. Designated Sponsor.
            3. Specialist.
            4. Quote provider.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=52,
            question="In which instruments is Xetra Midpoint trading permitted?",
            choices="""
            1. Bonds
            2. Shares
            3. Exchange Traded Funds
            4. Exchange Traded Commodities
            """,
            answer=["2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=53,
            question="In auctions time price/time priority is valid so that the maximum of one order, which is either limited at the auction price or unlimited, can be partially executed.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=54,
            question="Trade-at-Close is triggered automatically after each closing auction.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""Trade at close (TaC) needs: [1] Successful Price Determination and [2] Positive Turnover 
            If there is Zero turnover then session is skipped.
            """
        ),
        QA(
            id=55,
            question="Iceberg orders do not participate with their full volume in auctions.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            The exchange system uses the entire, overall volume of the Iceberg order when calculating the highest executable volume and determining the official auction price. 
            If only the small visible peak were used, the determined price would not accurately reflect the actual supply and demand.
            """
        ),
        QA(
            id=56,
            question="Which statement regarding pre- or post-trading phase is correct?",
            choices="""
            1. Market Participants can see the order book situation without restrictions.
            2. Market participants can enter, modify and delete orders and quotes during the pre-trading phase.
            3. Market participants can enter, modify and delete orders for the next trading day.
            4. The indicative auction price of the opening call is displayed during the pre-trading phase.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=57,
            question="Which statement regarding the trading models offered on the trading venue Xetra is wrong?",
            choices="""
            1. The call phase of an auction is partially closed.
            2. On-Exchange Off-Book transactions with any order volume can be executed.
            3. Auction price determination is effected according to the principle of most executable volume.
            4. The order book in continuous trading is open.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=58,
            question="Xetra on-exchange trading is supplemented by various functionalities. Which one is not included?",
            choices="""
            1. Request-for-Quote Functionality Xetra EnLight
            2. A functionality for off-book trading (T7 Entry Service - TES Typ LIS)
            3. Block trading functionality Xetra XXL
            4. A functionality to enter OTC transactions (T7 Entry Service - TES Typ OTC)
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            The trading venue Xetra offers several functionalities to supplement on-exchange trading, including:
            1. Request-for-Quote Functionality Xetra EnLight: This allows traders to request quotes from market makers for specific securities.
            2. A functionality for off-book trading (T7 Entry Service - TES Typ LIS): This enables the execution of large in scale (LIS) trades off the main order book.
            3. A functionality to enter OTC transactions (T7 Entry Service - TES Typ OTC): This allows for the entry of over-the-counter (OTC) transactions.
            However, Xetra does not include a specific "Block trading functionality Xetra XXL." 
            Block trades are typically large trades that are executed outside of the regular order book to minimize market impact, but there is no dedicated "XXL" functionality for this purpose on Xetra.
            """,
        ),
        QA(
            id=59,
            question="The duration of the random end for an auction call phase in the trading model continuous trading in connection with auctions is:",
            choices="""
            1. 0-30 Seconds
            2. 15 Seconds
            3. Only a few seconds
            4. Minimum of 15, maximum of 30 seconds
            """,
            answer="1",
            answer_type="single",
        ),
        QA(
            id=60,
            question="Which statement does not apply to Trade-at-Close (Tac)?",
            choices="""
            1. TaC starts only if the price determination in the closing auction was completed with a positive turnover.
            2. There is no pre-trade transparency, the order book is closed.
            3. New incoming orders that can be executed at the closing auction price are matched immediately.
            4. Only market and limit orders are allowed.
            """,
            answer="2",
            answer_type="single",
            comment_hint="""
            Trade-at-Close (TaC) is a trading mechanism that occurs after the closing auction.
            During TaC, there is pre-trade transparency, meaning that market participants can see the
            order book and the prices at which trades can be executed.
            The order book **is open for participants** to enter new orders or modify existing ones.
            """,
        ),
        QA(
            id=61,
            question="Which statement regarding auctions is correct?",
            choices="""
            1. The order book is open during the call phase.
            2. The order book is partially closed during the call phase.
            3. It ends in a freeze phase after the maximum duration of its call phase at the latest.
            4. Market surpluses are not displayed.
            """,
            answer="2",
            answer_type="single",
            comment_hint="""
            During the call phase of an auction, the order book is partially closed.
            This means that while new orders can still be entered, modified, or deleted,
            the existing orders are not visible to market participants.
            This partial closure helps to prevent market manipulation and ensures a fair price discovery process.
            """,
        ),
        QA(
            id=62,
            question="Which statement applies to continuous trading in connection with auctions?",
            choices="""
            1. A closing auction is only carried out for instruments included in a selection index.
            2. The duration of the call phase is different for opening auctions, intraday auctions and closing auctions.
            3. There is no fixed auction schedule.
            4. An opening auction is only carried out if the order book is crossed.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=63,
            question="Which statement applies to an auction?",
            choices="""
            1. In an auction, price/time priority applies.
            2. Book-or-cancel orders and volume discovery orders with the execution condition "GTX" are deleted when an auction is triggered.
            3. Iceberg orders and volume discovery orders participate with their full volume
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=64,
            question="Which statement regarding continuous trading is wrong?",
            choices="""
            1. Each order is fully executed with one transaction.
            2. Between market orders time priority applies.
            3. Continuous trading is started after the termination of the opening auction.
            4. New orders are checked for Self Match Prevention.
            """,
            answer="1",
            answer_type="single",
            comment_hint="""
            In continuous trading, orders can be partially executed through multiple transactions until the entire order volume is fulfilled.
            Therefore, the statement that each order is fully executed with one transaction is incorrect.
            """,
        ),
        QA(
            id=65,
            question="Which order types are supported on the trading venue Xetra?",
            choices="""
            1. Iceberg Orders.
            2. Hidden Orders.
            3. Stop Limit Orders.
            4. All-or-None Orders.
            """,
            answer=["1", "3"],
            answer_type="multiple",
            comment_hint="""
            The trading venue Xetra supports Iceberg Orders and Stop Limit Orders.
            Hidden Orders and All-or-None Orders are not supported on Xetra.
            """,
        ),
        QA(
            id=66,
            question="In which of the following cases does a modification of a limit order not result in a new time priority?",
            choices="""
            1. If the limit is changed.
            2. If the text field is changed.
            3. If the volume of the order is reduced.
            4. If the order modification has an adverse effect on the execution priority of other orders in the order book.
            """,
            answer=["2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=67,
            question="Which statements regarding the functionality of volume discovery orders are correct?",
            choices="""
            1. The total volume is executable against iceberg orders.
            2. The volume discovery order builds on the functionality of the iceberg order.
            3. The hidden part will only be executed at the current midpoint against other hidden parts of volume discovery orders.
            4. The order type can only be used in auctions.
            """,
            answer=["2", "3"],
            answer_type="multiple",
            comment_hint="""
            Volume discovery orders are designed to reveal a portion of their total volume over time, similar to iceberg orders.
            However, they have unique characteristics:
            1. They build on the functionality of iceberg orders, meaning they have a visible peak and a hidden part.
            2. The hidden part of a volume discovery order can be executed at the current midpoint against other hidden parts of volume discovery orders.
            The other statements are incorrect:
            1. The total volume of a volume discovery order is not executable against iceberg orders;
            2. Volume discovery orders can be used in both continuous trading and auctions, not just in auctions.
            """
        ),
        QA(
            id=68,
            question="In which of the following cases the overall volume of an iceberg order is visible during an auction?",
            choices="""
            1. Always.
            2. If, in the case of an uncrossed order book, the total volume of the iceberg order is part of the displayed cumulative volumes at the best bid/ask limit.
            3. If the total volume of the iceberg order is part of the indicative auction surplus.
            4. Never.
            """,
            answer=["2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=69,
            question="Which order types are supported in continuous trading?",
            choices="""
            1. Hidden order
            2. Iceberg order
            3. Volume Discovery order
            4. Order-on-event
            """,
            answer=["2", "3"],
            answer_type="multiple",
            comment_hint="""
            Hidden orders are not supported in continuous trading. They are only supported in auctions.
            Order-on-event is not a supported order type on the Xetra trading venue.
            Iceberg orders and Volume Discovery orders are supported in continuous trading.
            """,
        ),
        QA(
            id=70,
            question="Which statements concerning book-or-cancel orders are correct?",
            choices="""
            1. They permit passive execution only.
            2. They are executed as well in volatility interruptions.
            3. They must have a predefined minimum volume.
            4. If immediate execution is possible, the order is rejected.
            """,
            answer=["1", "4"],
            answer_type="multiple",
            comment_hint="""
            Book-or-cancel orders are designed for passive execution only, meaning they will only be executed
            if they can be matched with an existing order in the order book. If immediate execution is possible, the order is rejected.
            They are not executed during volatility interruptions, as trading is typically halted during such periods.
            There is no requirement for book-or-cancel orders to have a predefined minimum volume.
            """,
        ),
        QA(
            id=71,
            question="In which of the following ways is a fill-or-kill order executed?",
            choices="""
            1. Immediate execution to the extent possible, deletion of the unexecuted part of the order.
            2. Only during auctions.
            3. Only if there are no iceberg orders in the order book.
            4. Immediately and fully or not at all.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=72,
            question="In which of the following ways is an immediate-or-cancel order executed?",
            choices="""
            1. Identical execution to that of ordinary limit or market orders.
            2. Immediate execution to the extent possible, deletion of the unexecuted part of the order.
            3. Immediate execution in full, or if this is not possible, deletion of the order.
            4. None of the above.
            """,
            answer="2",
            answer_type="single",
            comment_hint="""
            An immediate-or-cancel order is executed by immediate execution to the extent possible, with the unexecuted part of the order being deleted. 
            This means that if only a portion of the order can be filled immediately, that portion will be executed, and the remainder will be canceled.   
            """
        ),
        QA(
            id=73,
            question="Which statement regarding modification of an order is correct?",
            choices="""
            1. A modification always leads to a new time priority.
            2. The order number remains always unchanged even if the order receives a new time priority.
            3. During auctions order modifications are not permissible.
            4. A modification effects a deletion of the existing order and a new order entry with new time priority and new order number.
            """,
            answer="2",
            answer_type="single",
            comment_hint="""
            When an order is modified, it does not always lead to a new time priority.
            The order number remains unchanged even if the order receives a new time priority.
            Order modifications are permissible during auctions.
            A modification does not result in the deletion of the existing order and the creation of a new order with a new order number.
            """
        ),
        QA(
            id=74,
            question="Which validity restriction does not exist for orders?",
            choices="""
            1. Good-for-day (GFD)
            2. Good-till-auction (GTA)
            3. Good-till-date (GTD)
            4. Good-till-cancelled (GTC)
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=75,
            question="Which of the following is correct for one-cancels-other orders?",
            choices="""
            1. It combines a market order and a stop order.
            2. It combines a limit order and a stop market order.
            3. All execution conditions and trading restrictions are supported.
            4. In case of a partial execution the non-executed parts of the order are deleted.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=76,
            question="Which of the following is correct for trailing stop orders?",
            choices="""
            1. If the reference price of a trailing stop sell order falls, the dynamic stop limit is not adjusted.
            2. Further execution conditions and trading restrictions are not supported.
            3. The dynamic stop limit is continuously monitored.
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=77,
            question="Which statement concerning the treatment of orders in the order book at a suspension or an interruption of trading is correct?",
            choices="""
            1. Unexecuted orders are deleted in both cases.
            2. Existing orders are deleted at a suspension of trading.
            3. Existing orders are deleted at an interruption of trading.
            4. Neither event has an influence on unexecuted orders.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=78,
            question="According to the Exchange Rules which specification is not necessary for order entry?",
            choices="""
            1. Orders generated through algorithmic trading have to be marked.
            2. Orders must have a member internal order number.
            3. There has to be an adequate ratio between order and bindings quotes entries, modifications and deletions and trades (Order to Trade Ratio).
            4. Orders need to be specified as proprietary or agent orders.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=79,
            question="Which of the following events does not lead to a deletion of orders?",
            choices="""
            1. Granting of subscription rights.
            2. Dividend payments.
            3. Significant price deviations from the last price.
            4. Suspension of trading.
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            Significant price deviations do not automatically delete orders; 
            they can trigger an order book suspension to allow the market to re-establish a fair price. 
            In contrast, corporate actions like dividend payments and granting of subscription rights often result 
            in adjustments or deletions of orders to prevent unfair gains or losses. 
            Trading suspensions also lead to order deletions to maintain market integrity during a halt.
            """
        ),
        QA(
            id=80,
            question="How does a midpoint sweep order behave if it has not found a counterparty in the midpoint order book?",
            choices="""
            1. The sweep order is automatically deleted.
            2. The sweep order remains in the midpoint order book and waits for execution.
            3. The sweep order is re-entered into the midpoint order book at a defined interval.
            4. The sweep order goes on to the open order book (Xetra Central Limit Orderbook) and checks for execution.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=81,
            question="The ACE volatility interruption model is assigned to all securities for all trading phases.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            The ACE volatility interruption model is not assigned to all securities for all trading phases.
            It is typically applied to specific securities or under certain market conditions, rather than universally across all
            securities and trading phases.
            """,
        ),
        QA(
            id=82,
            question="A volatility interruption can be initiated only if the potential next price lies outside both price ranges.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            it can be outside of either price ranges [1] Dynamic Corridor , [2] Static Corridor
            """,
        ),
        QA(
            id=83,
            question="A volatility interruption in continuous trading leads to a change in the trading form, in both the single volatility interruption model and the ACE volatility interruption model.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=84,
            question="Which of the following prices lead to an adjustment of the reference price for the static price corridor?",
            choices="""
            1. Auction prices
            2. Prices resulting from a volatility interruption
            3. Prices determined in continuous trading
            4. Indicative auction prices
            """,
            answer=["1", "2"],
            answer_type="multiple",
            comment_hint="""
            The reference price for the static price corridor is adjusted based on auction prices and prices resulting from
            a volatility interruption. 
            Prices determined in continuous trading and indicative auction prices do not lead to an adjustment of the reference price.
            """,
        ),
        QA(
            id=85,
            question="Which statements apply to one or both volatility interruption models?",
            choices="""
            1. In the ACE volatility interruption model several subsequently expanding price corridors can line up in the call phase.
            2. A volatility interruption is only triggered if the next potential execution price is outside the static price corridor.
            3. Price corridors are not published in the ACE volatility interruption model.
            4. An extended volatility interruption will be terminated automatically once there is no longer an executable order book situation.
            """,
            answer=["1", "4"],
            answer_type="multiple",
        ),
        QA(
            id=86,
            question="What leads to a volatility interruption in both volatility interruption models?",
            choices="""
            1. The indicative price lies outside the dynamic price range and within the static price range.
            2. The indicative price lies within the dynamic price range and outside the static price range.
            3. The indicative price lies outside the dynamic and the static price range.
            4. The indicative price corresponds to the reference price.
            """,
            answer=["1", "2", "3"],
            answer_type="multiple",
            comment_hint="""
            The dynamic price range is a narrow band around the last traded price. 
            A violation occurs when the indicative price is either above or below this moving range.
            The static price range is a wider band around a longer-term reference price, such as the closing price of the last auction. 
            This range provides a larger buffer for price movements.
            A volatility interruption is initiated if the indicative price lies outside *either* of these ranges
            """
        ),
        QA(
            id=87,
            question="Designated Sponsors have to provide double-sided quotes or orders for a certain minimum time during continuous trading.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
            comment_hint="""
            Designated Sponsors (DS) on Xetra are market makers who have the obligation to provide liquidity by continuously quoting 
            both buy and sell prices (double-sided quotes) or placing corresponding orders for a certain minimum time during continuous trading.
            This obligation helps to ensure that there is always a market for the securities they are responsible for, thereby enhancing market liquidity and stability.
            """,
        ),
        QA(
            id=88,
            question="For Designated Sponsor quotes all validity constraints are possible.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            For Designated Sponsor quotes, only the validity constraints Good-for-day (GFD) and Good-till-cancelled (GTC) are possible.
            """,
        ),
        QA(
            id=89,
            question="Only Designated Sponsors can enter quotes.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
            comment_hint="""
            Not only Designated Sponsors can enter quotes. 
            Other market participants, such as liquidity providers or
            traders with specific roles, may also enter quotes depending on the market structure and regulations.
            """,
        ),
        QA(
            id=90,
            question="Which of the following obligations has a Designated Sponsor?",
            choices="""
            1. In case of “stressed market conditions” stricter quote requirements.
            2. Provision of additional liquidity for at least 50 shares.
            3. Participation in auctions and volatility interruptions.
            4. Provision of liquidity by double-sided quotes or corresponding orders for certain minimum times during continuous trading.
            """,
            answer=["3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=91,
            question="A quote by a Designated Sponsor is ...",
            choices="""
            1. the non-binding indication of a price level.
            2. typically, the simultaneous entry of a buy and sell limit order.
            3. valid in continuous trading only.
            4. good for day.
            """,
            answer=["2", "4"],
            answer_type="multiple",
            comment_hint="""
            A quote by a Designated Sponsor is typically the simultaneous entry of a buy and sell limit order.
            It is good for day (GFD) or good-till-cancelled (GTC).
            A quote is a binding indication of a price level; it represents firm orders.
            It can be valid in both continuous trading and auctions.
            """,
        ),
        QA(
            id=92,
            question="What are the duties of Designated Sponsors?",
            choices="""
            1. Provision of additional liquidity
            2. Responding to quote requests by entering quotes
            3. Setting reference prices
            4. Involvement in auctions by entering quotes
            """,
            answer=["1", "2", "4"],
            answer_type="multiple",
            comment_hint="""
            Designated Sponsors (DS) on Xetra are market makers whose main duties are to enhance liquidity 
            (1) by providing continuous quotes and responding to quote requests . 
            (2) They are also required to participate in auctions .  
            (4) by entering quotes to ensure robust price discovery . 
            They do not set the official market reference prices (3) . 
            """
        ),
        QA(
            id=93,
            question="In which of the following cases is the reference price considered for stipulating the auction price?",
            choices="""
            1. If there is a surplus of offerings, which is not caused by a market order.
            2. If there is a surplus of demand, which is not caused by a market order.
            3. If there are several possible limits and there is both an ask surplus and a bid surplus.
            4. If there are several possible limits and there is no surplus on hand.
            """,
            answer=["3", "4"],
            answer_type="multiple",
            comment_hint="""
            In a **Xetra auction**, the system determines the optimal price that maximizes the executed volume. 
            However, when multiple prices could clear the maximum volume, or in cases where the order book is perfectly balanced (no surplus), 
            the system needs a **tie-breaker rule** to select the final auction price.
            The reference price is used precisely in these ambiguous scenarios, specifically 
                - (3) if there are several possible limits and there is both an ask surplus and a bid surplus 
                (meaning the surpluses cancel each other out at the maximum volume price),
            and  (4) if there are several possible limits and there is no surplus on hand (a perfectly balanced book).
            """
        ),
        QA(
            id=94,
            question="In addition to the maximum executable order volume, which of the following criteria are also used to determine the auction price:",
            choices="""
            1. Reference price
            2. Volume-weighted average of limits contained in the order book
            3. Surplus
            4. Theoretical price derived from a benchmark (e.g. EURO STOXX 50 Future)
            """,
            answer=["1", "3"],
            answer_type="multiple",
        ),
        QA(
            id=95,
            question="If during the call phase of an auction no price can be determined, what information is shown?",
            choices="""
            1. The lowest bid limit with volume
            2. The highest bid limit with volume
            3. The lowest ask limit with volume
            4. The highest ask limit with volume
            """,
            answer=["2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=96,
            question="What is the auction price based on the following auction order book situation? \n The reference price is 340. Tick Size 1 €.",
            choices="""
            1. 339
            2. 342
            3. 343
            4. None of the above
            """,
            answer="3",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_96.png"),
        ),
        QA(
            id=97,
            question="What is the auction price based on the following auction order book situation? \n The reference price is 340. Tick Size 1 €.",
            choices="""
            1. 341
            2. 340
            3. 342
            4. 343
            """,
            answer="3",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_97.png"),
        ),
        QA(
            id=98,
            question="What is the auction price based on the following auction order book situation? \n The reference price is 181. Tick Size 1 €.",
            choices="""
            1. 180
            2. 181
            3. 182
            4. None of the above.
            """,
            answer="2",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_98.png"),
        ),
        QA(
            id=99,
            question="Which execution(s) result(s) from the incoming market order (reference price 182) -sell 5,000 - in this order book in continuous trading?",
            choices="""
            1. 5.000 at 178.
            2. 5.000 at 180.
            3. 1.500 at 180 and 3.500 at 178.
            4. 3.500 at 180 and 1.500 at 178.
            """,
            answer="4",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_99.png"),
        ),
        QA(
            id=100,
            question="Which execution(s) result(s) from the incoming market order (reference price 179) - sell 5,000 - in this order book in continuous trading?",
            choices="""
            1. No execution - volatility interruption.
            2. No execution until a limit order is entered.
            3. Full execution of both market orders at the reference price.
            4. None of the above.
            """,
            answer="3",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_100.png"),
        ),
        QA(
            id=101,
            question="Which execution(s) result(s) from the incoming immediate-or-cancel order -sell 5,000, limit 9.10 - in this order book in continuous trading?",
            choices="""
            1. 5,000 at 9.08.
            2. 1,500 at 9.10.
            3. No execution, the order is placed in the order book.
            4. No execution, the order is rejected without entry in the order book.
            """,
            answer="4",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_101.png"),
        ),
        QA(
            id=102,
            question="Which execution(s) result(s) from the incoming limit order -buy 500, limit 23 - in this order book in continuous trading?",
            choices="""
            1. 500 at 21.90.
            2. 500 at 23.
            3. 120 at 22.50, 280 at 22.95 and 100 at 23.
            4. 100 at 22.50, 100 at 22.95 and 300 at 23.
            """,
            answer="3",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_102.png"),
        ),
        QA(
            id=103,
            question="Which execution(s) result(s) from the incoming fill-or-kill order - sell 5,000, limit 23 - in this order book in continuous trading?",
            choices="""
            1. 500 at 23.
            2. 500 at 23 and 4,500 at 22.95.
            3. 5,000 at 22.90.
            4. No execution.
            """,
            answer="4",
            answer_type="single",
            link_pic=os.path.join(start_path, "img", "question_103.png"),
        ),
        QA(
            id=104,
            question="How are market orders executed in continuous trading if they encounter an order book with only market orders on the opposite order book side?",
            choices="""
            1. At the highest bid or lowest ask limit in the order book.
            2. At the lowest bid or highest ask limit in the order book.
            3. At the reference price.
            4. None of the above.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=105,
            question="Participants require a separate admission for off-book trading.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=106,
            question="Xetra EnLight Smart Respondents receive request for quotes (RfQs) when their willingness to submit an offer calculated for the specific ISIN is high.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=107,
            question="Off-book transactions concluded via the T7 entry service must have a minimum volume (large-in-scale) determined by the management board of the FWB.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=108,
            question="Which of the following statements apply to the Continuous Auction with Specialist?",
            choices="""
            1. There is exactly one specialist per security.
            2. The specialist can enter orders in the securities assigned to him in his own name and, if a corresponding order exists, also on behalf of other trading participants.
            3. During the main trading phase, the order book is fully open to market participants (order book depth 10).
            4. The quote provider is able to identify the originator of an order.
            """,
            answer=["1", "2"],
            answer_type="multiple",
        ),
        QA(
            id=109,
            question="Which of the following statements apply to the Continuous Auction with Specialist?",
            choices="""
            1. Execution conditions (FOK or IOC) are not supported.
            2. Stop orders are triggered by a matching quote.
            3. The matching quote is deleted after price determination.
            4. Only orders valid Good-for-day are permitted.
            """,
            answer=["1", "2", "3"],
            answer_type="multiple",
            comment_hint="""
            Execution conditions like FOK (Fill or Kill) or IOC (Immediate or Cancel) are not supported in this model. 
            Stop orders are triggered by a matching quote from the specialist, not by an executed trade price, 
            and the matching quote used to initiate the price determination is deleted once the auction is completed.
            """
        ),
        QA(
            id=110,
            question="Which of the following statements apply to stop orders in the trading model Continuous Auction with Specialist?",
            choices="""
            1. A stop-loss order is triggered if the bid limit of the matching quote is equal to or below the stop limit.
            2. A stop-loss order is triggered when the last price is equal to or below the stop limit.
            3. Stop Limit and Stop Market Orders are supported.
            4. Stop orders in the order book are visible to all trading participants.
            """,
            answer=["1", "3"],
            answer_type="multiple",
        ),
        QA(
            id=111,
            question="In the Continuous Auction with Specialist trading model, the order book is ...",
            choices="""
            1. completely open during the main trading phase (order book depth 10).
            2. closed during the pre-trading phase.
            3. is partially closed during the pre-trading phase.
            4. is closed during the post-trading phase.
            """,
            answer=["3", "4"],
            answer_type="multiple",
            comment_hint="""
            In the Continuous Auction with Specialist model, the order book's visibility *changes* with each trading phase.
            > During the pre-trading phase, the order book is partially closed (Choice 3), meaning only the *best bid and ask prices* are visible to the public. 
            > During the post-trading phase, all trading has concluded, and the *order book is closed* (Choice 4) to new order entry and execution.
            """
        ),
        QA(
            id=112,
            question="Which statements apply to quotes in the Continuous Auction with Specialist?",
            choices="""
            1. They can have a quantity greater than or equal to zero.
            2. In principle, they must be double-sided (bid and ask).
            3. The specialist should consider fixed minimum quotation volumes and maximum spreads.
            4. The specialist can modify or delete standard quotes (indicative quotes).
            """,
            answer=["1", "2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=113,
            question="What roles are there in the trading model Continuous auction with specialist?",
            choices="""
            1. Specialist
            2. Quote Provider
            3. Liquidity Provider
            4. Designated Sponsor
            """,
            answer=["1", "2"],
            answer_type="multiple",
        ),
        QA(
            id=114,
            question="Which securities are traded in the Continuous Auction?",
            choices="""
            1. Mutual Funds
            2. Exchange Traded Funds
            3. Bonds
            4. Shares
            """,
            answer=["1", "2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=115,
            question="Which of the following statements do not apply to the Continuous Auction?",
            choices="""
            1. There are several specialists per security.
            2. There are volatility interruptions to ensure price continuity.
            3. Orders are executed according to price/time priority.
            4. The specialist can identify the originator of an order.
            """,
            answer=["1", "2"],
            answer_type="multiple",
            comment_hint="There is exactly one specialist per security. There are no volatility interruptions in the Continuous Auction with Specialist.",
        ),
        QA(
            id=116,
            question="Which of the following statements about the Continuous Auction with Specialist are correct?",
            choices="""
            1. After price determination, unexecuted parts of the specialist quote remain in the order book.
            2. The matching quote (binding quote) is deleted after price determination.
            3. The price is determined according to modified principle of highest executable volume.
            4. Orders in the order book are executed according to volume/time priority.
            """,
            answer=["2", "3"],
            answer_type="multiple",
            comment_hint="""
            The Continuous Auction with Specialist model is designed for less liquid securities and has unique rules.
            A specialist's matching quote is a one-time trigger for price determination, 
            and the price is always set to maximize the volume of trades, not based on order entry time.
            """
        ),
        QA(
            id=117,
            question="How is the price determined in the Continuous Auction with Specialist?",
            choices="""
            1. According to the modified principle of highest executable volume exclusively to the bid or ask limit of the matching quote.
            2. According to the modified principle of highest executable volume corresponding to or within the price range determined by the matching quota.
            3. According to the modified principle of highest executable volume, only within the range determined by the matching quote.
            4. According to the modified principle of highest executable volume, only within the price range determined by the order book.
            """,
            answer="2",
            answer_type="single",
        ),
        QA(
            id=118,
            question="How are stop loss orders triggered in the Continuous Auction with Specialist?",
            choices="""
            1. If the ask limit of the matching quote equals or falls below the stop limit.
            2. If the ask limit of the matching quote equals or exceeds the stop limit.
            3. If the bid limit of the matching quote equals or exceeds the stop limit.
            4. If the bid limit of the matching quote equals or falls below the stop limit.
            """,
            answer="4",
            answer_type="single",
            comment_hint="the matching quote was low enough to trigger the stop limit.",
        ),
        QA(
            id=119,
            question="How are stop buy orders triggered in the Continuous Auction with Specialist?",
            choices="""
            1. If the bid limit of the matching quote equals or falls below the stop limit.
            2. If the bid limit of the matching quote equals or exceeds the stop limit.
            3. If the ask limit of the matching quote equals or exceeds the stop limit.
            4. If the ask limit of the matching quote equals or falls below the stop limit.
            """,
            answer="3",
            answer_type="single",
            comment_hint="the matching quote was high enough to trigger the stop limit.",
        ),
        QA(
            id=120,
            question="In the “Continuous Auction with Specialist” trading model, trading participants can enter a quote request for which the corresponding quote of the specialist and the order placed thereupon relate directly to each other and can be assigned to each other by means of a quote ID.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
            comment_hint=" a unique quote ID links the request, the specialist's quote, and the resulting order, ensuring a clear audit trail."
        ),
        QA(
            id=121,
            question="The Specialist may enter orders in his own name and in the securities assigned to him for other trading participants.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
            comment_hint="""
            A Specialist on a stock exchange has a unique role that includes managing liquidity and supporting the market for the securities they are assigned. 
            Part of this role grants them the authority to not only enter orders on their own behalf 
            but also to act as an agent for other trading participants, entering orders for them in the specialist's assigned securities.
            """
        ),
        QA(
            id=122,
            question='In the "Continuous Auction with Specialist" trading model, several specialists can assume the indicative quotation for a security.',
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=123,
            question="Provided that a Special Auction is scheduled, it is performed once a day.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
            comment_hint="""Special Auction can be executed multiple times a day. 
            If a Special Auction is scheduled, it is performed at least once a day.""",
        ),
        QA(
            id=124,
            question="Specialists initiate a separate auction for orders with the trading restriction Special Auction.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=125,
            question="For certain securities, the specialist conducts a single auction only once a day.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=126,
            question="There are no Single auctions in the Continuous Auction Specialist model.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=127,
            question="Which statements on the transparency of the order book apply to the Continuous Auction with Specialist?",
            choices="""
            1. During the freeze phase the order book is fully open for the Specialist.
            2. During the pre-call phase the order book is partially closed for the Specialist.
            3. During the freeze phase the order book is completely closed.
            4. During the pre-call phase the order book is partially closed for trading participants.
            """,
            answer=["1", "4"],
            answer_type="multiple",
        ),
        QA(
            id=128,
            question="How are prices determined in a Continuous Auction with Specialist?",
            choices="""
            1. The price is determined by the trading system.
            2. The price determination process is triggered by the specialist entering a matching quote (binding quote).
            3. If there are several eligible limit steps and the consideration of the surplus does not lead to a clear auction price, the midpoint of the eligible limit steps is included as additional criterion.
            4. The auction price is determined on the basis of the matching quote and the order book situation stipulated at the end of the freeze phase.
            """,
            answer=["1", "2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=129,
            question="What statements apply to structured products when a knock-out occurs or a threshold is breached?",
            choices="""
            1. The ISIN is temporarily suspended from trading after the occurrence of the event.
            2. Once the suspension has been lifted, only sell orders can be entered until the maturity date or until the delisting of the security concerned.
            3. The specialist must report the event immediately.
            4. The specialist is only allowed to enter single-sided quotes for repurchasing the securities.
            """,
            answer=["1", "2", "4"],
            answer_type="multiple",
            comment_hint="""
            In the event of a knock-out or threshold breach for structured products, trading is typically suspended to prevent disorderly market conditions. 
            After the suspension is lifted, only sell orders are generally permitted to allow investors to exit their positions. 
            The specialist plays a crucial role in managing the market for these securities during such events,
            often entering single-sided quotes to facilitate repurchasing.
            """,
        ),
        QA(
            id=130,
            question="Which of the following statements are applicable for Continuous Auctions with Specialist?",
            choices="""
            1. After the freeze phase a price determination or a phase change to the pre-call phase is possible.
            2. During the pre-call phase, the order book is only completely open to the specialist, i.e. the specialist can view each order and quote request and the respective originator.
            3. Orders that are entered during the freeze phase are stored and will enter the order book immediately after it gets unlocked.
            4. After price determination any remaining parts of the Specialist quote are not deleted.
            """,
            answer=["1", "2", "3"],
            answer_type="multiple",
        ),
        QA(
            id=131,
            question="For which of the following security types a Special Auction can be executed by the Specialists?",
            choices="""
            1. Subscription rights
            2. Mutal funds
            3. German Government Bonds
            4. Covered warrants
            """,
            answer=["1", "3"],
            answer_type="multiple",
            comment_hint="""
            Special Auctions on the Xetra platform (which uses the Specialist model for certain securities) are typically reserved for security types 
            that might have lower trading volumes or require specific handling outside the standard continuous trading mechanisms,
            especially for larger orders. 
            The correct answers are Subscription rights (1) and German Government Bonds (3). 
            Subscription rights often have a short trading life and unique liquidity needs, making the auction a practical mechanism. 
            German Government Bonds (Bunds) can also be subject to Special Auctions to ensure orderly execution of large block trades outside 
            the standard order book, complementing the high-volume, but often fragmented, bond market.
            """
        ),
        QA(
            id=132,
            question="What kind of order types are available in the trading model continuous auction with Specialist?",
            choices="""
            1. Stop order
            2. Market-to-Limit order
            3. Iceberg order
            4. One-cancels-Other order
            """,
            answer=["1", "4"],
            answer_type="multiple",
            comment_hint="""In the Continuous Auction with Specialist trading model, stop orders and one-cancels-other orders are available
            as order types. 
            Market-to-limit orders and iceberg orders are not supported in this trading model.
            """,
        ),
        QA(
            id=133,
            question="In the trading model Continuous Auction with Specialist, the Specialist is responsible for a high trading quality. Which of the following duties arise from this task?",
            choices="""
            1. Incoming quote requests are to be responded to without delay.
            2. Information that has become known in connection with the activities as a Specialist shall not be disclosed to third parties.
            3. Continuous provision of non-binding quotes based on the current market situation (order situation incl. reference market)
            4. Use of a limit control system to continuously check the executability of the orders on hand
            """,
            answer=["1", "2", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=134,
            question="Which statements are applicable for a freeze phase of a Continuous Auction with Specialist?",
            choices="""
            1. Only the Specialist quote is displayed.
            2. It has a random end.
            3. The Specialist is able to enter orders on own behalf or on behalf of other trading participants and can modify or delete these orders.
            4. There is no predetermined minimum period.
            """,
            answer=["1", "3", "4"],
            answer_type="multiple",
            comment_hint="""
            During the freeze phase, the order book is frozen. 
            During the freeze phase, the system collects order inputs, changes and deletions in a “suspended portfolio” until the freeze is lifted, whereupon they are immediately processed.
            """,
        ),
        QA(
            id=135,
            question="Which statements are applicable for a pre-call phase of a Continuous Auction with Specialist?",
            choices="""
            1. Trading participants cannot enter orders.
            2. The order book is completely open.
            3. The specialist can enter, modify or delete own orders and he can enter or delete orders on behalf of other trading participants.
            4. The specialist may enter or delete quotes.
            """,
            answer=["3", "4"],
            answer_type="multiple",
            comment_hint="""The pre-call phase allows all trading participants to enter **orders**, 
            but the book is **partially closed**, showing **only the best bid/ask prices**. 
            During this time, the specialist has unique access to manage the order book, including the ability to enter, modify, and delete their own orders and quotes.
            """,
        ),
        QA(
            id=136,
            question="What must the exchange trader acting on behalf of a specialist basically do if the expected price of a share whose last price was greater than €5.00 differs by more than 10 per cent?",
            choices="""
            1. Enter an adjusted standard quote (non-binding quote) and start the freeze phase (or “call phase” according to the Exchange Rules) only after a period of 5 minutes.
            2. Enter an adjusted matching quote (binding quote) and start the freeze phase only after a period of 10 minutes.
            3. Enter an adjusted standard quote (non-binding quote) and start the freeze phase only after a period of 15 minutes.
            4. Enter an adjusted standard quote (non-binding quote) and start the pre-call phase only after a period of 10 minutes.
            """,
            answer="1",
            answer_type="single",
            comment_hint="""
            When a share's expected price differs by more than 10 pct from its last price, 
            the specialist must enter a new non-binding quote and initiate a "freeze phase" that lasts for 5 minutes before trading can resume. 
            This pause allows the market to react to the new price before a new auction or continuous trading begins.
            """
        ),
        QA(
            id=137,
            question="What must the exchange trader acting on behalf of a Specialist consider when determining a price without turnover?",
            choices="""
            1. A price without turnover (PWT) quote shall only be entered after 12:00 pm CET.
            2. A PWT quote shall only be entered if a standard quote (non-binding quote) without volume was entered before.
            3. A PWT quote shall only be entered if a standard quote (non-binding quote) with volume was entered before.
            4. None of the above.
            """,
            answer="3",
            answer_type="single",
        ),
        QA(
            id=138,
            question="Which of the following statements are applicable for quote-request driven trading in Continuous Auction with Specialist?",
            choices="""
            1. If there is no adequate quote (e.g., due to lack of volume), quote requests may be rejected with a corresponding error message.
            2. The quote request must contain a numeric value, the so-called quote ID.
            3. The quote answer of the specialist and the order based upon that answer refer directly to each other and can be assigned to each other by means of the quote ID.
            4. All of the above.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=139,
            question="Which of the following duties do not apply to an exchange trader acting on behalf of a specialist?",
            choices="""
            1. In the case of securities that are traded in foreign currency and settled in euros, in addition to entering the matching quote (binding quote) for conversion, an exchange rate in line with the market must be entered.
            2. Ensure that at least one price is determined per trading day for each security.
            3. In order to restart trading after a suspension, a "Special Auction" shall be conducted.
            4. During trading hours, continuously provide standard quotes (non-binding quotes) on the basis of the current order situation, taking into account any reference market.
            """,
            answer="3",
            answer_type="single",
            comment_hint="""
            To restart trading after a suspension, a "Special Auction" is not always required. 
            The specialist may choose to resume trading through a standard auction process or other mechanisms as defined by exchange rules, 
            depending on the circumstances of the suspension.
            """
        ),
        QA(
            id=140,
            question="Which minimum requirements must the limit control system of the specialist fulfil?",
            choices="""
            1. Permanent monitoring of all new and existing orders in the order book with regard to their executability.
            2. Immediate display of stop loss orders if they have reached the bid limit of the standard quote (indicative quote).
            3. Immediate indication of the executability of orders (market and limit orders) in the order book against the standard quote (indicative quote) or against other orders.
            4. All of the above mentioned requirements.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=141,
            question="Which entry is not possible for the Specialist during the freeze phase?",
            choices="""
            1. Order entry on behalf of other trading participants.
            2. Entry of an exchange rate.
            3. Own order entry
            4. Entry of a standard quote.
            """,
            answer="4",
            answer_type="single",
            comment_hint="""
            During the freeze phase, the specialist can no longer enter a standard quote because trading is temporarily halted. 
            This period is specifically for order entry and other administrative tasks before the market reopens, not for quoting prices. 
            Therefore, the ability to submit a standard quote is disabled.
            """
        ),
        QA(
            id=142,
            question="If there is no executable order book situation, a price without turnover can be generated on the basis of the bid side of the specialist quote.",
            choices="""
            1. True
            2. False
            """,
            answer="1",
            answer_type="true_false",
        ),
        QA(
            id=143,
            question="In the Continuous Auction, the auction price is determined solely on the basis of the specialist quote.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=144,
            question="If the consideration of the surplus in the Continuous Auction does not lead to a clear auction price, the reference price is used as a further criterion.",
            choices="""
            1. True
            2. False
            """,
            answer="2",
            answer_type="true_false",
        ),
        QA(
            id=145,
            question="How is the auction price determined in the Continuous Auction with Specialist?",
            choices="""
            1. The average value of all limits available at the end of the call Phase will be the auction price.
            2. Within a price range specified by Cash Markets Operations.
            3. Within the price range specified by the specialist's quote (including the bid/ask limit of the quote).
            4. Based on the specialist quote and the order book position fixed at the end of the freeze phase.
            """,
            answer=["3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=146,
            question="How is a price without turnover determined in the specialist model?",
            choices="""
            1. Cash Markets Operations determines the price.
            2. Price determination is triggered by entering a separate quote (price-without-turnover quote).
            3. After entering a price-without-turnover quote, the price without turnover is generated on the basis of the bid side of the quote.
            4. The price is calculated from the average value of the available order limits.
            """,
            answer=["2", "3"],
            answer_type="multiple",
            comment_hint="""
            In the Continuous Auction with Specialist model, a price without turnover is determined when there are no executable orders in the book. 
            This process is initiated by the specialist entering a specific quote designated for price without turnover.
            The price is then calculated based on the bid side of that quote, reflecting the specialist's assessment of the market value in the absence of trades.
            """
        ),
        QA(
            id=147,
            question="What are the basic rules for price determination in Continuous Auction with Specialist?",
            choices="""
            1. The auction price is determined according to the modified principle of highest executable volume.
            2. The auction price is determined by the specialist.
            3. If no executable orders are available, it is not possible to determine an auction price with turnover.
            4. The auction price is determined by the trading system.
            """,
            answer=["1", "3", "4"],
            answer_type="multiple",
        ),
        QA(
            id=148,
            question="What happens in Continuous Auction with Specialist if there is more than one limit step with the highest executable order volume and the lowest surplus?",
            choices="""
            1. If, for each of the limit steps, the surplus lies within the price range (including the bid and ask limits of the specialist quote) on the bid side, the auction price is calculated according to the highest of these limit steps.
            2. The auction price is determined by the specialist.
            3. No auction price can be determined.
            4. None of the above answers is correct.
            """,
            answer="1",
            answer_type="single",
        ),
        QA(
            id=149,
            question="When does a Continuous Auction with Specialist result in a price without turnover?",
            choices="""
            1. If the price variance from the last price exceeds a certain percentage.
            2. If the security is suspended from trading.
            3. If the surplus in the order book is too large at the time of price determination.
            4. If a corresponding quote has been entered and there is no executable order book situation.
            """,
            answer="4",
            answer_type="single",
        ),
        QA(
            id=150,
            question="What happens if the consideration of the surplus in a price determination of a Continuous Auction with Specialist does not lead to a clear auction price?",
            choices="""
            1. The reference price is used to determine the auction price.
            2. The auction price is determined by the specialist.
            3. The midpoint is calculated of the highest eligible limit step with surplus on the bid side and the lowest eligible limit step with surplus on the ask side and serves as auction price.
            4. None of the above answers is correct.
            """,
            answer="3",
            answer_type="single",
        ),
    ]
