POST spec
=========
This refers in part to the diagram, available as `pay_plan_rn.png` (where n is the revision) in the `planning` folder of this repo.  
__All requests, unless otherwise specified, are `POST`.__

It's noted some of this is unclear, so it will be more thoroughly documented once the system is implemented, with example code given in varying languages.

_Requests are specified as a Ruby hash-table here, purely for effect; these variables should be sent as a POST query._
## Step `1.`
```ruby
# Customer -> Seller
# This is variable, the seller can handle it
# however they like.
{
    :order => :some_item_id,
    :blah => foo
}
```

## Step `2.`
```ruby
# Seller -> Pay
{
    :price => n,
    :api_key => :my_key,
    :listen_url => "http://seller.listen/url",
    :payout_addr => "seller.payout.addr",

    # Seller can set sell_x variables which are stored
    # and sent to Seller when the payment goes through.
    :sell_foo => "something"
}
```

## Step `3.`
```ruby
# Pay -> BLC
{
    :cmd => :register,
    :addr => "PAY-SOME123TRANSACTION123ADDR",
    :pwd => :random_pwd
}
```

## Step `3a.`
```ruby
# Pay -> Seller
{
    :address => "PAY-SOME123TRANSACTION123ADDR",
    :price => n,
    :txn_id => id,
}
```

## Step `4.`
```ruby
# Seller -> Customer (front end)
{
    :address => "PAY-SOME123TRANSACTION123ADDR"
    :price => n
}
```

## Step `4a.` (looping)
```ruby
# Pay -> BLC
# Repeatedly querying the amount of coins we have
{
    :cmd => :check_addr,
    :addr => "PAY-SOME123TRANSACTION123ADDR"
}
```

## Step `5.`
```ruby
# Customer -> BLC
# Customer pays Pay's transaction address
{
    :cmd => :send_coins,
    :to => "PAY-SOME123TRANSACTION123ADDR",
    :addr => :my_addr,
    :pwd => :my_pwd,
    :amount => n
}
```

## Step `6.`
```ruby
# Pay -> Seller
{
    :amount => n,
    :from => :from_addr,
    :txn_id => id,

    # All the variables the Seller gave to Pay
    :sell_foo => "something"
}
```

## Step `6a.`
```ruby
# Seller -> Pay (reverse for confirmation)
{
    :_confirm => :anything,
    :amount => n,
    :from => :from_addr,
    :txn_id => id

    # All the variables the Seller gave to Pay
    :sell_foo => "something"
}
```

## Step `6b.`
```ruby
# Pay -> BLC (paying Seller)
{
    :cmd => :send_coins,
    :to => :seller_payout,
    :amount => n,
    :addr => "PAY-SOME123TRANSACTION123ADDR",
    :pwd => :random_pwd
}
```

## Step `7.`
Seller activates Customer's service, informs Customer via some medium.
