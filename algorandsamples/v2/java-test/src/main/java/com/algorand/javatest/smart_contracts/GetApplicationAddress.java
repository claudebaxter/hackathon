package com.algorand.javatest.smart_contracts;

import com.algorand.algosdk.crypto.Address;

public class GetApplicationAddress {
    public void getApplicationAddressExample() throws Exception {
        Long appId = 95223182L ;
        Address actual = Address.forApplication(appId);
        System.out.println("Address: " + actual.toString());
    }


public static void main(final String args[]) throws Exception {
    GetApplicationAddress t = new GetApplicationAddress();
    t.getApplicationAddressExample();}}