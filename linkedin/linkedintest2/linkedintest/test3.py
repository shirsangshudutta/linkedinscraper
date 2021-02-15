from bs4 import BeautifulSoup
html="""<ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
<li id="ember268" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="351623021" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/jadavpur-university/" id="ember271" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQFkGVsBobrK1A/company-logo_100_100/0?e=1597881600&amp;v=beta&amp;t=mqpmL8hKvUlmUnewWcwbg9NP5qPtnPMfuEeOJ8Q9C8M" loading="lazy" alt="Jadavpur University" id="ember273" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section mb2">
  <h3 class="t-16 t-black t-bold">Associate Professor</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Jadavpur University
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Sep 2006 – Present</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">13 yrs 9 mos</span>
      </h4>
  </div>

<!---->
<!---->
</div>

</a>
        <div id="ember275" class="pv-entity__extra-details t-14 t-black--light ember-view"><p style="line-height:2rem;max-height:16rem;" id="ember276" class="pv-entity__description t-14 t-black t-normal inline-show-more-text inline-show-more-text--is-collapsed ember-view">Teaching UG and PG students, guiding PG thesis, research

<!----></p><!----></div>
    </div>

<!---->  </div>
</section>
</li><li id="ember278" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="351625532" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/wipro/" id="ember281" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C510BAQGmX81XFwCcFg/company-logo_100_100/0?e=1597881600&amp;v=beta&amp;t=w1GuS5JIpfpPUJnScwvkxvnlTlS2oxtZQkDu773WmZI" loading="lazy" alt="Wipro Technologies" id="ember283" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section mb2">
  <h3 class="t-16 t-black t-bold">Project Engineer</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Wipro Technologies
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Sep 2005 – Sep 2006</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 1 mo</span>
      </h4>
  </div>

<!---->
<!---->
</div>

</a>
        <div id="ember285" class="pv-entity__extra-details t-14 t-black--light ember-view"><p style="line-height:2rem;max-height:8rem;" id="ember286" class="pv-entity__description t-14 t-black t-normal inline-show-more-text inline-show-more-text--is-collapsed ember-view">Software development

<!----></p><!----></div>
    </div>

<!---->  </div>
</section>
</li><li id="ember288" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="351971126" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/search/results/all/?keywords=Centre%20for%20Mobile%20Computing%20and%20Communication%20(CMCC)%2C%20Jadavpur%20University" id="ember291" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Centre for Mobile Computing and Communication (CMCC), Jadavpur University" id="ember293" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ghost-company ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Research Fellow</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Centre for Mobile Computing and Communication (CMCC), Jadavpur University
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Jul 2004 – Jun 2005</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li>  </ul> """
html_soup = BeautifulSoup(html,'lxml')

exp=html_soup.find_all("div", {"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"})
print(exp)