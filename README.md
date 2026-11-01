This is an economic simulation of a free market. As the name suggests, it is a simulation that deals with the price of goods. In the end it generates a day-by-day report of the buying and selling prices of all buyers and sellers

Firstly, there are 2 classes, a buyer and a seller Each maintains a stock, the seller of a product and buyer of inventory

Each has an ep a price at which they are comfortable to buy

If the seller ep is lower than buyer ep then buyer immediately buys from that seller at the sellers ep

They also have an mp. For seller it is mp if buyer offeres lower than mp they will not sell For buyer it is maximum price and if higher than that is offered by any seller, they will immediately leave the market in most simulations

It is a useful tool in studying the impact of supply and demand in economics

There are a few versions each adding a feature over base version

Here are a chocie few:-

1. bargaining_version.py
   the most advanced and most modern sim. It has features of all previous sims along with a new bargaining system. If seller ep is greater than buyer ep, then they will haggle and bargain. The amount of bargaining depends on buyers bargaining ep. Also sellers can resist bargain and can cause customers to overpay due to their own bargaining ep
   This system is more accurate in simulating a street market where bargaining is allowed
2. base_version_with_user_input.py
   The most basic version. It has no stock. Each buyer and seller has only ep and mp. It is the most basic but acts as a solid foundation for all future versions
3. buyer_seller_stock_v.py
   A version bulit on base where both buyers and sellers have modifiable stock with them

This sim works on latest python version as well

Future improvements include adding a matplotlib graph
